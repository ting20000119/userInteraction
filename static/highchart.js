function myFunc(arr){

var jjson = [{'sometime_statue': 'Jons312', 'count': 2},
{'Jons312': 'Nyrfan2017', 'count': 1},
{'Jons312': 'AA', 'count': 1}]

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
        for (var i = 0; i < jjson.length; i++) {
        const keys = Object.keys(jjson[i]);
        //console.log(keys[0] + "HI");
          if(this.key === keys[0]){
            info = info + ' '+ jjson[i][this.key] + ':' +  jjson[i]['count'] ;
        }
       }
      
     /* if(this.key === "Busan"){
        info = jjson[0][this.key] + jjson[0]['count']  +  jjson[2][this.key] + jjson[2]['count'];
      }*/
      
      /*switch (this.key) {
        case "Busan":
          info = jjson[0][this.key] + jjson[0]['count']  +  jjson[2][this.key] + jjson[2]['count'];
          break; 
        case "Jeju":
          info = jjson.length;
          break;
      }*/
      
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

