

myApp = angular.module("myApp.controllers", []);

myApp.controller("Main", function($scope, $http){

    //id of the current user
    $scope.current_user_id = 1;
    $scope.current_user = "";



    var route = "/get_user_with_id/" + $scope.current_user_id;

    $http.get(route).success(function(data){
        $scope.current_user = data["name"];
    });



});
