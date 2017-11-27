/**
 * Created by symenyang on 2017/5/14.
 */
function ShowBox(d)
{
    box.showBox(d);
}


var nodes = [ { name: "开始" , proc : 1  }, { name: "赋值" , proc :1  },
    { name: "条件语句" , proc : 1  }, { name: "循环语句" , proc : 0.75  },
    { name: "函数" , proc : 0.65  }, { name: "局部变量" , proc : 0  },
    { name: "全局变量" , proc : 0.75  } ];


var edges = [  { source : 0  , target: 1 } , { source : 0  , target: 2 } ,
    { source : 0  , target: 3 } , { source : 0  , target: 4 } ,
    { source : 0  , target: 5 } , { source : 0  , target: 6 } ,
    { source : 1  , target: 2 } ];


// Get the offset
var width = 2000;
var height = 2000;
var localwidth = screen.availWidth;
var localheight = screen.availHeight;
var offsetx = Math.max(0,(width - localwidth)/2);
var offsety = Math.max(0,(height - localheight)/2);

//zoom part
var svgmove = d3.behavior.zoom().scaleExtent([1, 1]).on("zoom", zoom);
svgmove.translate([-offsetx,-offsety]);
function zoom() {
    svg.attr("transform", "translate(" + d3.event.translate + ")scale(" + d3.event.scale + ")");
}


//define the svg
var svg = d3.select("body")
    .append("svg")
    .attr("width",width)
    .attr("height",height)
    .append("g")
    .call(svgmove)
    .attr("transform", "translate(" + -offsetx + "," + -offsety + ")scale(1)");

//zoom rect
svg.append("rect")
    .attr("class", "overlay")
    .attr("width", width)
    .attr("height", height);

var force = d3.layout.force()
    .nodes(nodes)		//指定节点数组
    .links(edges)		//指定连线数组
    .size([width,height])
    .linkDistance(55)	//指定连线长度
    .charge(-2500)
    .gravity(-0.01)
    .friction(0.9);
// init the position of nodes
var p = force.nodes();
p[0].fixed = true;
p[0].x = width / 2;
p[0].y = height / 2;
var l = p.length;
for (var i = 1;i < l; ++i)
{
    p[i].x = width / 2 + Math.random() * 100;
    p[i].y = height / 2 + Math.random() * 100;
}
force.alpha(0.5).start();


//first layer
var svg0 = svg.append("g");

var svg_edges = svg0.selectAll("line")
    .data(edges)
    .enter()
    .append("line")
    .style("stroke","#d7c713")
    .style("stroke-width",2);

var svg_nodes = svg0.selectAll("circle")
    .data(nodes)
    .enter()
    .append("circle")
    .attr("r",40)
    .style("stroke","#d7c713")
    .style("stroke-width",2)
//    .call(force.drag)
    .style("fill",function(d,i){
        // return "#8248c9";
        return "#4e1892";
    })
    .on("click",function (d,i) {
        Reloc(d,i,0);
    });

//second layer
var svg1 = svg.append("g");

var svg_nodes_in = svg1.selectAll("circle")
    .data(nodes)
    .enter()
    .append("circle")
    .attr("r",function (d) {
        return d.proc * 40;
    })
//    .call(force.drag)
    .style("fill",function(d,i){
//        if (d.proc == 1)
        return "#d7c713";

    })
    .on("click",function (d,i) {
        Reloc(d,i,0);
    });

//third layer
var svg2 = svg.append("g");

var svg_texts = svg2.selectAll("text")
    .data(nodes)
    .enter()
    .append("text")
    .style("fill", "#fefefe")
    .attr("dy", 4)
    .style("text-anchor", "middle")
    .text(function(d){
        return d.name;
    })
 //   .call(force.drag)
    .on("click",function(d,i){
        var reloc = localwidth / 2 - 150;
        Reloc(d,i,-reloc);
        ShowBox(d);
    });

function Reloc(d,i,pos)
{
    var dx = width / 2 - p[i].x + 1;
    var dy = height / 2 - p[i].y + 1;
    for (var j = 0;j < l; ++j)
    {
        p[j].x = p[j].x + dx;
        p[j].y = p[j].y + dy;
        p[j].px = p[j].x;
        p[j].py = p[j].y;
        if (j != 0)
        {
            p[j].fixed = false;
        }
    }
    p[i].px = p[i].x;
    p[i].py = p[i].y;
    p[i].fixed = true;
    force.alpha(0.1);
    svg.attr("transform", "translate(" + (pos - offsetx) + "," + -offsety + ")scale(1)");
    svgmove.translate([pos - offsetx,-offsety]);
}

force.on("tick", function(){
    svg_edges.attr("x1",function(d){ return d.source.x; })
        .attr("y1",function(d){ return d.source.y; })
        .attr("x2",function(d){ return d.target.x; })
        .attr("y2",function(d){ return d.target.y; });
    svg_nodes_in.attr("cx",function(d){ return d.x; })
        .attr("cy",function(d){ return d.y; });
    svg_nodes.attr("cx",function(d){ return d.x; })
        .attr("cy",function(d){ return d.y; });
    svg_texts.attr("x", function(d){ return d.x; })
        .attr("y", function(d){ return d.y; });
});