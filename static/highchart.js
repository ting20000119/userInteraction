function myFunc(arr , jjson){


console.log(jjson);

Highcharts.chart("container", {
  chart: {
    type: "networkgraph",
    marginTop: 80
  },

  title: {
    //text: "r/politics interaction"
  },

 
  tooltip: {
    useHTML: true,
    style: {
      pointerEvents: 'auto'
    },
    formatter: function () {
      var info = "";
      count = 0 ;
      for (var i = 0; i < jjson.length; i++) {
        const keys = Object.keys(jjson[i]);
        keys.forEach(key => {
          if(this.key === key && count < 3){
            count = count + 1;
            info = info + ' '+ jjson[i][this.key] + ':' +  jjson[i]['count'] ;
          }
        });
      }
      if(count == 0){
      return "<b>" + "No reply" + "</b>" ;
     }
     else{
      return "<b>" + "Most frequently replied" + "</b>: " + info + "\n" + '<a href="http://www.google.com">click</a>';
     }
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

