function myFunc(arr){
console.log(arr);
Highcharts.chart("container", {
  chart: {
    type: "networkgraph",
    marginTop: 80
  },

  title: {
    //text: "r/politics interaction"
  },

  tooltip: {
    formatter: function () {
      var info = "";
      switch (this.color) {
        case "#E8544E":
          //console.log("rep");
          //info = "rep";
          break;
        case "#0000ff":
          //console.log("dem");
          //info = "dem";
          break;
          case "#808080":
            //console.log("error");
            //info = "error";
            break;
      }
      return "<b>" + this.key + "</b>: " + info;
    }
  },

  plotOptions: {
    networkgraph: {
      keys: ["from", "to"],
      layoutAlgorithm: {
        enableSimulation: true,
        integration: "verlet",
        linkLength: 100
      }
    }
  },
  series: arr
});
}

