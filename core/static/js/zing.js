var myConfig = {
  "type": "line3d",
  "series": [{
    "values": [20, 40, 25, 50, 15, 45, 33, 34]
  }, {
    "values": [5, 30, 21, 18, 59, 50, 28, 33]
  }, {
    "values": [30, 5, 18, 21, 33, 41, 29, 15]
  }]
};
 
zingchart.render({
  id: 'myChart',
  data: myConfig,
  height: "100%",
  width: "100%"
});