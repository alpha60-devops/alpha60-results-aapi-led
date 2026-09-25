// Native Izzi / Cartofreako city-share comparison panels.
// Geometry is clipped at registered CK seams before projection; holes are kept.
#include "izzi-svg.h"
#include "ck-native.h"
#include <rapidjson/document.h>
#include <fstream>
#include <iomanip>
#include <limits>

using std::string;
using point = std::pair<double, double>;
using ring = std::vector<point>;
using polygon = std::vector<ring>;
using geometry = std::vector<polygon>;

string number(double x) { std::ostringstream s; s << std::fixed << std::setprecision(3) << x; return s.str(); }
string escape(const string& s) { return svg::escape_xml_attribute(s); }
rapidjson::Document read(const char* path) {
  std::ifstream f(path);
  if (!f) throw std::runtime_error(string("cannot read ") + path);
  string text((std::istreambuf_iterator<char>(f)), {});
  rapidjson::Document d; d.Parse(text.c_str());
  if (d.HasParseError()) throw std::runtime_error("invalid JSON");
  return d;
}
void text(svg::svg_element& svg, double x, double y, const string& value, int size=18) {
  svg.add_raw("<text x=\""+number(x)+"\" y=\""+number(y)+"\" font-family=\"DejaVu Sans,sans-serif\" font-size=\""+std::to_string(size)+"\" fill=\"#26313a\">"+escape(value)+"</text>");
}
void rectangle(svg::svg_element& svg, double x,double y,double w,double h,const string& fill) {
  svg.add_raw("<rect x=\""+number(x)+"\" y=\""+number(y)+"\" width=\""+number(w)+"\" height=\""+number(h)+"\" fill=\""+fill+"\"/>");
}
int main(int argc, char** argv) {
  if (argc != 4) return 2;
  auto boundaries=read(argv[1]), data=read(argv[2]);
  a60::carto::ck_native::forward_projection forward(1056);
  auto project=[&](double lon,double lat) -> point {
    lon += 1; if(lon>180) lon-=360;
    const auto [x,y]=forward(lon,lat); return {2112+x,1056-y};
  };
  const int n=data["countries"].Size(), columns=n==3?3:2, rows=(n+columns-1)/columns;
  const double width=1200, panel_width=(width-60)/columns, panel_height=440, height=rows*panel_height+180;
  svg::svg_element svg(argv[3], svg::area<>{width,height});
  rectangle(svg,0,0,width,height,"white");
  text(svg,24,32,data["title"].GetString(),24);
  text(svg,24,61,data["subtitle"].GetString(),17);
  for(int i=0;i<n;++i) {
    const auto& country=data["countries"][i];
    const string code=country["code"].GetString();
    geometry polygons;
    double x0=1e99,y0=1e99,x1=-1e99,y1=-1e99;
    auto bound=[&](point p){x0=std::min(x0,p.first);x1=std::max(x1,p.first);y0=std::min(y0,p.second);y1=std::max(y1,p.second);};
    for(const auto& c:boundaries["countries"].GetArray()) if(code==c["iso3"].GetString()) {
      for(const auto& poly:c["geometry"]["coordinates"].GetArray()) {
        polygon out;
        for(const auto& r:poly.GetArray()) {
          ring result;
          for(const auto& p:r.GetArray()) { auto xy=project(p[0].GetDouble(),p[1].GetDouble()); bound(xy);result.push_back(xy); }
          out.push_back(result);
        }
        polygons.push_back(out);
      }
    }
    if(polygons.empty()) throw std::runtime_error("missing country "+code);
    std::vector<point> cities;
    for(const auto& p:country["points"].GetArray()) {
      auto xy=project(p["coordinates"][0].GetDouble(),p["coordinates"][1].GetDouble());bound(xy);cities.push_back(xy);
    }
    const double left=20+(i%columns)*panel_width, top=100+(i/columns)*panel_height;
    text(svg,left+12,top-8,country["name"].GetString(),21);
    rectangle(svg,left+5,top,panel_width-10,panel_height-48,"#f2f5f7");
    const double s=std::min((panel_width-42)/(x1-x0),(panel_height-84)/(y1-y0));
    const double tx=left+panel_width/2-s*(x0+x1)/2,ty=top+(panel_height-48)/2-s*(y0+y1)/2;
    auto xy=[&](point p) {return number(tx+s*p.first)+" "+number(ty+s*p.second);};
    for(const auto& poly:polygons) {
      string d;
      for(const auto& r:poly) {bool first=true;for(point p:r){d+=(first?"M":"L")+xy(p);first=false;}d+="Z";}
      svg.add_raw("<path d=\""+d+"\" fill=\"white\" fill-rule=\"evenodd\" stroke=\"#86939b\" stroke-width=\"0.6\"/>");
    }
    for(rapidjson::SizeType j=0;j<country["points"].Size();++j) {
      const auto& p=country["points"][j];const double delta=p["delta"].GetDouble();
      const auto [cx,cy]=cities[j];const double x=tx+s*cx,y=ty+s*cy,sign=delta>0?1:-1;
      const double ratio=std::min(1.0,std::abs(delta)/data["scale"].GetDouble());
      const int end[2][3]={{23,91,140},{164,71,18}};const int k=delta>0?1:0;
      string color="rgb(";for(int q=0;q<3;++q)color+=(q?",":"")+std::to_string(int(235+(end[k][q]-235)*ratio));color+=")";
      string d="M"+number(x)+" "+number(y-8*sign)+" L"+number(x-7)+" "+number(y+5*sign)+" L"+number(x+7)+" "+number(y+5*sign)+" Z";
      const string tip=escape(p["tooltip"].GetString());
      svg.add_raw("<path d=\""+d+"\" fill=\""+color+"\" stroke=\"#26313a\" stroke-width=\"1\" tabindex=\"0\" role=\"img\" aria-label=\""+tip+"\" data-tooltip=\""+tip+"\"><title>"+tip+"</title></path>");
    }
  }
  text(svg,24,height-65,"Orange upward: first object higher; blue downward: second object higher. Shared identified cities only.",16);
  text(svg,24,height-40,"Color magnitude: 0 to "+number(data["scale"].GetDouble())+" percentage points; same scale across this page.",16);
  text(svg,24,height-15,"Izzi / Cartofreako Cahill–Keyes · countries fitted separately · lake water excluded · vector outlines",15);
}
