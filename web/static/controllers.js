

myApp = angular.module("myApp.controllers", []);

myApp.controller("Main", function($scope, $http, $location){

    $scope.current_user_id = 1;
    $scope.current_user = "";
    
    if($location.path() == "/" || $location.path() == "/home"){
        $scope.current_page = "/home";
    }
    if($location.path() == "/add_class"){
        $scope.current_page = "/add";
    }
    else{
        $scope.current_page = "/home";
    }

    var route = "/get_user_with_id/" + $scope.current_user_id;

    $http.get(route).success(function(data){
        $scope.current_user = data["name"];
    });

    $scope.show_home_page = function(){
        $scope.current_page = "/home";
    }

    $scope.show_add_class_page = function(){
        $scope.current_page = "/add";
    }


});



myApp.controller("homeCtrl", function($scope, $http){


    $scope.get_user_classes = function(){

        var route = '/get_user_classes/' + $scope.current_user_id;
        $http.get(route).success(function(data){
            alert(data);
            $scope.classes = data;
        });

    }

    $scope.get_user_classes();


});


myApp.controller("addClassCtrl", function($scope, $http, $location){

    //change the path, come back to this later
    //$location.path('/add_class');


    $scope.validate_class_fields = function(){
        if($scope.class_name == null || $scope.class_name == ''){
            alert("Please Enter a class name");
            return false;
        }
        if($scope.homework_freq == null || $scope.homework_freq == ''){
            alert("Please enter a homework frequency");
            return false;
        }
        return true;
    }

    
    $scope.add_class = function(){
        
        if($scope.validate_class_fields()){
            
            var route = "/add_class_to_db";
            var parms = {
                user_id : $scope.current_user_id,
                class_name : $scope.class_name,
                homework_freq : $scope.homework_freq
            };
            $http.get(route, {params : parms}).success(function(data){
                alert(data);
            });
        }
    }


});


