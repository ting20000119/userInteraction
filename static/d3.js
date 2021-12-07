function myFunc(json){

var width = 3000,
    height = 3000

var svg = d3.select("body").append("svg")
    .attr("width", 1500)
    .attr("height", 900);

var force = d3.layout.force()
    .gravity(0.25)
    .distance(100)
    .charge(-100)
    //.linkDistance(12)//線的距離長度
    .size([950, 750]);

console.log(json);

  force
      .nodes(json.nodes)
      .links(json.links)
      .start();

  var link = svg.selectAll(".link")
      .data(json.links)
    .enter().append("line")
      .attr("class", "link")
      .style("stroke", function(d){ if(d.position == "same") {return 'orange'} else {return 'green'} }) 
    .style("stroke-width", function(d) { return Math.sqrt(d.count); });


  var node = svg.selectAll(".node")
      .data(json.nodes)
    .enter().append("g")
      .attr("class", "node")
      .call(force.drag);
      

  node.append("circle").style("fill", function (d) { return d.leaning; })
      .attr("r","10");

  node.append("text")
      .attr("dx", 12)
      .attr("dy", ".35em");
      //.text(function(d) { return d.author });

  force.on("tick", function() {
    link.attr("x1", function(d) { return d.source.x; })
        .attr("y1", function(d) { return d.source.y; })
        .attr("x2", function(d) { return d.target.x; })
        .attr("y2", function(d) { return d.target.y; });

    node.attr("transform", function(d) { return "translate(" + d.x + "," + d.y + ")"; });
  });
}

