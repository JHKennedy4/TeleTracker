<?php
$con=mysqli_connect("localhost","testuser","qwerty123","test");
// Check connection
if (mysqli_connect_errno())
  {
  echo "Failed to connect to MySQL: " . mysqli_connect_error();
  }

// $nextMonth = time(Y-m-d) + (30 * 24 * 60 * 60);
// $nextMonth = date('Y-m-d', $nextMonth);
// $lastMonth = time(Y-m-d) - (4 * 12 * 30 * 24 * 60 * 60);
// $lastMonth = date('Y-m-d', $lastMonth);

$result = mysqli_query($con,"SELECT start_time, end_time, target FROM events WHERE id < 100"); #WHERE start_time BETWEEN \"$nextMonth\" AND \"$lastMonth\"

// in the reply we must fill in the request id that came with the request
$reqId = getReqId();
echo "
google.visualization.Query.setResponse({
  version:'0.6',
  reqId:'$reqId',
  status:'ok',
  table:{
    cols:[{id:'start',
           label:'',
           type:'datetime'},
          {id:'end',
           label:'',
           type:'datetime'},
          {id:'content',
           label:'',
           type:'string'}
         ],
    rows:[";

    while($row = mysqli_fetch_array($result))
  {
      #echo print_r ($row);
      $start_year = substr($row['start_time'], 0, 4);
      $start_month = substr($row['start_time'], 5, 2);
      $start_day = substr($row['start_time'], 8, 2);

      $end_year = substr($row['end_time'], 0, 4);
      $end_month = substr($row['end_time'], 5, 2);
      $end_day = substr($row['end_time'], 8, 2);

      $target = $row['target'];


      echo "{c:[{v:new Date($start_year, $start_month, $start_day)}, {v:new Date($end_year, $end_month, $end_day)}, {v:'$target'}]},";
  }
echo "]
  }
});
";



/**
 * Retrieve the request id from the get/post data
 * @return {number} $reqId       The request id, or 0 if not found
 */ 
function getReqId() {
  $reqId = 0;

  foreach ($_REQUEST as $req) {
    if (substr($req, 0,6) == "reqId:") {
      $reqId = substr($req, 6);
    }
  }

  return $reqId;
}

mysqli_close($con);

?>
