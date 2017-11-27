/**
 * Created by symenyang on 2017/5/21.
 */
function ShowBox(d)
{
    box.showBox(d);
}


var nodes = [];

var edges = [];

var width = 4000;
var height = 4000;
var localwidth = screen.availWidth;
var localheight = screen.availHeight;
var offsetx = Math.max(0,(width - localwidth)/2);
var offsety = Math.max(0,(height - localheight)/2);

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
    .attr("width", width * 2)
    .attr("height", height * 2);

var force = d3.layout.force()
    .nodes(nodes)		//指定节点数组
    .links(edges)		//指定连线数组
    .size([width,height])
    .linkDistance(105)	//指定连线长度
    .charge(-750)
    .gravity(0.00)
    .chargeDistance(1000)
    .linkStrength(0.9);



// init the position of nodes
var p = force.nodes();
var l = 0;
if (p.length != 0){
    p[0].fixed = true;
    p[0].x = width / 2;
    p[0].y = height / 2;
    l = p.length;
    for (var i = 1;i < l; ++i)
    {
        p[i].x = width / 2 + Math.random() * 100;
        p[i].y = height / 2 + Math.random() * 100;
    }
}

force.alpha(1.0).start();


//first layer
var svg0 = svg.append("g");

var svg_edges = svg0.selectAll("line");

var svg_nodes = svg0.selectAll("circle");

//second layer
var svg1 = svg.append("g");

var svg_nodes_in = svg1.selectAll("circle");

//third layer
var svg2 = svg.append("g");

var svg_texts = svg2.selectAll("text");

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
//        if (j != 0)
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
    force.alpha(0.1);
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

var position = [];

function record(){
    var l = p.length;
    for (var i = 0;i < l;++i) {
        position.push({cx : p[i].x , cy : p[i].y , px : p[i].px , py : p[i].py});
    }
    console.log(position[1]);
}

function recordBack(){
    var l = p.length;
    for (var i = 0;i < l;++i){
        p[i].x = position[i].cx;
        p[i].y = position[i].cy;
        p[i].px = position[i].px;
        p[i].py = position[i].py;
    }
    while (position.length != 0)
        position.pop();
}

function addData(name){
    axios.post('/api/getDAG',{
            username : name
    })
    .then(function (response) {
        var l = response.data.length;
        for (var j = 0;j < l;++j)
        {
            nodes.push({ID:response.data[j].ID,name:response.data[j].name,proc:response.data[j].proc,type:response.data[j].type});
        }
    });

    axios.get('/api/getRelation')
    .then(function (responce) {
        var l = responce.data.length;
        for (var k = 0;k < l;++k)
        {
            edges.push({source:responce.data[k].source , target: responce.data[k].target});
        }
        update();
        recordBack();
        console.log(p[1]);
    });
}

function clean() {
    record();
    while (nodes.length != 0){
        nodes.pop();
    }
    t = 0;
    while (edges.length != 0){
        edges.pop();
    }
    svg_edges = svg_edges.data(edges);
    svg_edges.exit().remove();

    svg_nodes = svg_nodes.data(nodes);
    svg_nodes.exit().remove();

    svg_nodes_in = svg_nodes_in.data(nodes);
    svg_nodes_in.exit().remove();

    svg_texts = svg_texts.data(nodes);
    svg_texts.exit().remove();
}

function update() {

    svg_edges = svg_edges.data(edges);
    svg_edges.enter()
        .append("line")
        .style("stroke","#e6db74")
        .style("stroke-width",3);

    svg_nodes = svg_nodes.data(nodes);
    svg_nodes.enter()
        .append("circle")
        .attr("r",40)
        .style("stroke","#e6db74")
        .style("stroke-width",2)
        .style("fill",function(d,i){
        if (d.type == 1){
            return "#919383";
        }
        return "#3e3d32";
    })
        .on("click",function (d,i) {
        Reloc(d,i,0);
    })
        .on("mouseover",function () {
            d3.select(this)
                .style("stroke-width",5)
                .style("stroke","#e9de77");
        })
        .on("mouseout",function () {
            d3.select(this)
                .style("stroke-width",2)
                .style("stroke","#e6db74");
        });

    svg_nodes_in = svg_nodes_in.data(nodes);
    svg_nodes_in.enter()
        .append("circle")
        .attr("r",function (d) {
        return d.proc * 0.40;
    })
        .style("fill",function(d,i){
        return "#e6db74";

    })
        .on("click",function (d,i) {
        Reloc(d,i,0);
    });

    svg_texts = svg_texts.data(nodes);
    svg_texts.enter()
        .append("text")
        .style("fill", "#f8f8f2")
        .attr("dy", 4)
        .style("text-anchor", "middle")
        .text(function(d){
        return d.name;
    })
        .on("click",function(d,i){
        var reloc = localwidth / 2 - 150;
        Reloc(d,i,-reloc);
        ShowBox(d);
    });
    p = force.nodes();
    l = 0;
    if (p.length != 0){
        p[0].fixed = true;
        p[0].x = width / 2;
        p[0].y = height / 2;
        l = p.length;
        for (var i = 1;i < l; ++i)
        {
            p[i].x = width / 2 + (Math.random() - 0.5) * 400;
            p[i].y = height / 2 + (Math.random() - 0.5) * 400;
        }
    }
    force.start();
}