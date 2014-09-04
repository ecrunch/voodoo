

myApp = angular.module("myApp.controllers", []);



myApp.controller("mainCtrl", function($scope){
    $scope.current_user = "Zack";
    $scope.current_user_id = 1;
});


myApp.controller("homeCtrl", function($scope, $http){

    var route = "/get_user_classes/" + $scope.current_user_id;
    $http.get(route).success(function(data){
        $scope.my_classes = data;  
    });  

});


myApp.controller("addClassCtrl", function($scope, $http){


    $scope.validate = function(){
        if($scope.class_name == null || $scope.class_name == ""){
            alert("Please enter a class name");
            return false;
        }
        if($scope.homework_freq == null || $scope.homework_freq == ""){
            alert("Please enter a homework freq");
            return false;
        }
        return true;
    }

    $scope.submit = function(){
        if(! $scope.validate()){
            return
        }

        var parms = {
            "user_id" : $scope.current_user_id,
            "class_name" : $scope.class_name, 
            "homework_freq" : $scope.homework_freq
        };

        $http.get("/add_class_to_db", {params : parms}).success(function(data){
            alert("Class added!");
        });

        

    }

});

