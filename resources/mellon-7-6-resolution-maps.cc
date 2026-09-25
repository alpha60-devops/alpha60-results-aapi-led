// Native Izzi / Cartofreako combined-resolution country detail plates.
// Inputs are lake-subtracted, seam-split geographic polygons and city weights.
#include "izzi-svg.h"
#include "ck-native.h"
#include <rapidjson/document.h>
#include <fstream>
#include <iomanip>
#include <numbers>

using std::string;
using point = std::pair<double, double>;
using ring = std::vector<point>;
using polygon = std::vector<ring>;

string number(double value) {
  std::ostringstream out; out << std::fixed << std::setprecision(6) << value;
  return out.str();
}
string precise(double value) {
  std::ostringstream out; out << std::setprecision(17) << value;
  return out.str();
}
string escape(const string& value) { return svg::escape_xml_attribute(value); }
rapidjson::Document read(const char* path) {
  std::ifstream input(path);
  if (!input) throw std::runtime_error(string("cannot read ") + path);
  string value((std::istreambuf_iterator<char>(input)), {});
  rapidjson::Document document; document.Parse(value.c_str());
  if (document.HasParseError()) throw std::runtime_error("invalid JSON");
  return document;
}
void text(svg::svg_element& canvas, double x, double y, const string& value,
          int size = 16, const string& extra = "") {
  canvas.add_raw("<text x=\"" + number(x) + "\" y=\"" + number(y)
    + "\" font-family=\"DejaVu Sans,sans-serif\" font-size=\"" + std::to_string(size)
    + "\" fill=\"#26313a\" " + extra + ">" + escape(value) + "</text>");
}
void circle(svg::svg_element& canvas, double x, double y, double radius,
            int group, const string& attributes = "") {
  svg::circle_element mark;
  mark.start_element(); mark.add_data({x, y, radius});
  mark.add_raw(group == 0
    ? " fill=\"#b53466\" fill-opacity=\"0.38\" stroke=\"none\" "
    : " fill=\"none\" stroke=\"#a94e00\" stroke-width=\"0.9\" ");
  mark.add_raw(attributes); mark.finish_element(); canvas.add_element(mark);
}
int main(int argc, char** argv) {
  if (argc != 4) return 2;
  auto boundaries = read(argv[1]), data = read(argv[2]);
  a60::carto::ck_native::forward_projection forward(1056);
  auto project = [&](double lon, double lat) -> point {
    lon += 1; if (lon > 180) lon -= 360;
    const auto [x, y] = forward(lon, lat); return {2112+x, 1056-y};
  };
  double x0=1e99, y0=1e99, x1=-1e99, y1=-1e99;
  auto bound = [&](point p) {
    x0=std::min(x0,p.first); x1=std::max(x1,p.first);
    y0=std::min(y0,p.second); y1=std::max(y1,p.second);
  };
  std::vector<polygon> polygons;
  const string code=data["code"].GetString();
  for (const auto& c: boundaries["countries"].GetArray()) if (code==c["iso3"].GetString()) {
    for (const auto& poly: c["geometry"]["coordinates"].GetArray()) {
      polygon out;
      for (const auto& r: poly.GetArray()) {
        ring projected;
        for (const auto& p: r.GetArray()) {
          auto xy=project(p[0].GetDouble(),p[1].GetDouble()); bound(xy); projected.push_back(xy);
        }
        out.push_back(projected);
      }
      polygons.push_back(out);
    }
  }
  if (polygons.empty()) throw std::runtime_error("missing country "+code);
  const double area=data["area_points_squared_per_weight"].GetDouble();
  auto radius=[&](double weight) { return std::sqrt(weight*area/std::numbers::pi); };
  double largest=0;
  std::vector<point> points;
  for (const auto& city: data["cities"].GetArray()) {
    const auto& p=city["coordinates"];
    auto xy=project(p[0].GetDouble(),p[1].GetDouble()); bound(xy); points.push_back(xy);
    for (const auto& mark: city["marks"].GetArray()) largest=std::max(largest,radius(mark["weight"].GetDouble()));
  }
  const double width=720, height=770, left=20, top=100, panel_width=680, panel_height=550;
  const double padding=std::max(24.,largest+5);
  const double scale=std::min((panel_width-2*padding)/(x1-x0),(panel_height-2*padding)/(y1-y0));
  const double tx=left+panel_width/2-scale*(x0+x1)/2, ty=top+panel_height/2-scale*(y0+y1)/2;
  auto xy=[&](point p) { return point{tx+scale*p.first,ty+scale*p.second}; };
  svg::svg_element canvas(argv[3],svg::area<>{width,height});
  canvas.add_raw("<rect width=\"720\" height=\"770\" fill=\"white\"/>");
  text(canvas,24,35,data["title"].GetString(),24);
  text(canvas,24,64,"Combined resolution swarms · weeks 1–26",18);
  text(canvas,24,86,"January 9–July 9, 2026 · weekly by-BTIH downloader weights",14);
  canvas.add_raw("<rect x=\"20\" y=\"100\" width=\"680\" height=\"550\" fill=\"#f2f5f7\"/>");
  canvas.add_raw("<g data-map-scale=\""+precise(scale)+"\" data-map-tx=\""+precise(tx)
    +"\" data-map-ty=\""+precise(ty)+"\">");
  for (const auto& poly: polygons) {
    string path;
    for (const auto& r: poly) {
      bool first=true;
      for (point p: r) {
        const auto [x,y]=xy(p); path+=(first?"M":"L")+number(x)+" "+number(y); first=false;
      }
      path+="Z";
    }
    canvas.add_raw("<path class=\"country-land\" d=\""+path
      +"\" fill=\"white\" fill-rule=\"evenodd\" stroke=\"#86939b\" stroke-width=\"0.5\"/>");
  }
  canvas.add_raw("</g>");
  // All filled marks precede all rings, so neither resolution obscures the other.
  for (int group=0; group<2; ++group) {
    for (rapidjson::SizeType i=0; i<data["cities"].Size(); ++i) {
      const auto& city=data["cities"][i]; const auto& mark=city["marks"][group];
      const auto weight=mark["weight"].GetUint64(); if (!weight) continue;
      const auto [x,y]=xy(points[i]); const string tip=escape(mark["tooltip"].GetString());
      const string attributes=" data-city-id=\""+escape(city["id"].GetString())
        +"\" data-resolution=\""+(group==0?"ge1080":"lt1080")+"\" data-weight=\""
        +std::to_string(weight)+"\" tabindex=\"0\" role=\"img\" aria-label=\""+tip
        +"\" data-tooltip=\""+tip+"\" ";
      circle(canvas,x,y,radius(weight),group,attributes);
    }
  }
  // Place four labels using non-overlapping candidate boxes within the panel.
  std::vector<std::array<double,4>> used;
  for (rapidjson::SizeType i=0; i<std::min<rapidjson::SizeType>(4,data["cities"].Size()); ++i) {
    const auto& city=data["cities"][i]; const string name=city["city"].GetString();
    const auto [x,y]=xy(points[i]); const double w=std::min(210.,name.size()*8.5+8);
    std::array<double,4> box{};
    for (point offset: std::vector<point>{{28,-32},{28,32},{-w-28,-32},{-w-28,32},{28,-64},{-w-28,64}}) {
      const double lx=std::clamp(x+offset.first,left+8,left+panel_width-w-8);
      const double ly=std::clamp(y+offset.second,top+24,top+panel_height-12);
      box={lx,ly-17,lx+w,ly+5};
      bool collision=false;
      for (const auto& b: used) if(box[0]<b[2]+5 && box[2]>b[0]-5 && box[1]<b[3]+5 && box[3]>b[1]-5) collision=true;
      if (!collision) break;
    }
    used.push_back(box);
    const double lx=std::clamp(x,box[0],box[2]),ly=box[1]+11;
    canvas.add_raw("<path d=\"M"+number(x)+" "+number(y)+" L"+number(lx)+" "+number(ly)
      +"\" fill=\"none\" stroke=\"#55616a\" stroke-width=\"0.6\"/>");
    text(canvas,box[0]+4,box[1]+17,name,15,"paint-order=\"stroke\" stroke=\"white\" stroke-width=\"4\" stroke-linejoin=\"round\"");
  }
  circle(canvas,40,682,8,0); text(canvas,58,688,"≥1080p (1080 + 2160)",16);
  circle(canvas,375,682,8,1); text(canvas,393,688,"<1080p (720 + SD)",16);
  circle(canvas,40,715,radius(10000),0);
  text(canvas,58,720,"10,000 weight = 120 pt² · one area scale across six plates",15);
  text(canvas,24,750,"Izzi / Cartofreako Cahill–Keyes · vector land with lake water removed",14);
}
