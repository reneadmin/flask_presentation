// https://observablehq.com/@attharmirza/mapping-vantage-points-during-an-open-source-investigatio

const WIDTH  				  = 900;
const HEIGHT  				= WIDTH*0.8;

  //MARGIN CONVENTION
  var MARGIN = {  LEFT  : 0, RIGHT: 0, TOP: 0, BOTTOM: 0 }
  var CANVAS = {  WIDTH : 1300  - MARGIN.LEFT - MARGIN.RIGHT,
                  HEIGHT: 1200  - MARGIN.TOP  - MARGIN.BOTTOM}
  
  const svg      = d3.select("#viz").append("svg")
              .attr("width" , CANVAS.WIDTH  + MARGIN.LEFT + MARGIN.RIGHT)
              .attr("height", CANVAS.HEIGHT + MARGIN.TOP  + MARGIN.BOTTOM)
                      .attr("version", "1.1")

  const svgCanvas = svg.append("g")
              .attr("transform", `translate(${MARGIN.LEFT}, ${MARGIN.TOP})`)
let  extent = {};
let data;


function dims ()  {
  let dimensions = {
    width: CANVAS.WIDTH,
    height: CANVAS.HEIGHT,
    marginTop: 175
  };

  dimensions.marginLeft = dimensions.marginTop;
  dimensions.marginBottom = dimensions.marginTop;
  dimensions.marginRight = dimensions.marginTop;

  dimensions.chartWidth =
    dimensions.width - dimensions.marginLeft - dimensions.marginRight;
  dimensions.chartHeight =
    dimensions.height - dimensions.marginTop - dimensions.marginBottom;

  return dimensions;
}

svgDims = dims();



function main()
{
  let personas = {};


  Promise.all ([
    d3.json('personas.json').then((resolve,reject) => {return resolve;}).then( (resolve, result) => {personas = resolve;  }),
    // d3.json('roads.geojson').then((resolve,reject) => {return resolve;}).then( (resolve, result) => {vectors.roads = resolve;  }),
    // d3.json('buildings.geojson').then((resolve,reject) => {return resolve;}).then( (resolve, result) => {vectors.buildings = resolve;  }),
    // d3.csv('zoom.geojson').then((resolve,reject) =>    { zoom = resolve;}),
    // d3.csv('demo.csv').then((resolve,reject) =>    { points = resolve;}),
    //fetch('Objects.xlsx')    .then(response => response.blob()).then(blob => readXlsxFile(blob, {sheet:1, schema: SCHEMAS[0] }).then((resolve,reject ) => {points = resolve.rows; console.log('points', points)})),

  ]
).then((resolve, reject) =>
{  
  
  
  drawChart(personas)
  
    }
  )
}

function drawChart(personas) {
  console.log('drawChart', personas)

  svgCanvas.selectAll('.Avatar')
  .data(personas)
  .join(
    enter => {
      enter.append('svg:image')
            .attr('x', 11)
            .attr('y', 300)
            .attr('width', 300)
            .attr("xlink:href", "/static/img/avatars/ManPresenter.png")


    },
    update => {},
    exit => {}
  )

  
}



main();