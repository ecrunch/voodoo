

myApp = angular.module("myApp", []);


myApp.controller("Main", function($scope){
    $scope.message = "Angular Works";   
})



myApp.controller("SchedulerCtrl", function($scope, $http){

    $scope.schedule = [{"timeslot" : "15", "item" : "reddit"}];

    //$scope.schedule = []


    //var scheduler = "/make_schedule";
    //$http.get(scheduler).success(function(data){
    //    alert(data[1]); 
    //    $scope.schedule = data;
    //});



});






