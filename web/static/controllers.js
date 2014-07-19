

myApp = angular.module("myApp", []);


myApp.controller("Main", function($scope){
    $scope.message = "Angular Works";   
})



myApp.controller("SchedulerCtrl", function($scope, $http){

    $scope.schedule = [{"time_slot" : "15", "description" : "reddit"}];

});






