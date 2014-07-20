

myApp = angular.module("myApp", []);


myApp.controller("Main", function($scope){
    $scope.message = "Angular Works";   
})



myApp.controller("SchedulerCtrl", function($scope, $http){


    $scope.schedule = [];
    $scope.hours = 4;

    $scope.selected_item = null;
    $scope.show_item = false;




    var scheduler = "/get_schedule/" + $scope.hours;
    $http.get(scheduler).success(function(data){ 
        $scope.schedule = data;
        $scope.header_hour = $scope.hours;
    });

    $scope.update_schedule = function update_schedule(){
        //alert("New schedule covering " + $scope.hours + " hours");

        var scheduler = "/get_schedule/" + $scope.hours;
         
        $http.get(scheduler).success(function(data){ 
            $scope.schedule = data;
            $scope.header_hour = $scope.hours;
            $scope.show_item = false;
        });

    }


    $scope.display_item = function display_item(item){

        $scope.selected_item = item;
        $scope.show_item = true;

    }




});



myApp.controller("InfoCtrl", function($scope, $http){


});






