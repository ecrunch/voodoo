

myApp = angular.module("myApp.controllers", []);



myApp.controller("mainCtrl", function($scope){
    $scope.current_user = "Zack";
    $scope.current_user_id = 1;
});


myApp.controller("homeCtrl", function($scope, $http){

    
    //refactor this into get user info or something like that
    //so we are only making one call

    var route = "/get_user_classes/" + $scope.current_user_id;
    $http.get(route).success(function(data){
        $scope.my_classes = data;  
    });  

    
    route = "/get_user_tasks/" + $scope.current_user_id;
    $http.get(route).success(function(data){
        $scope.my_tasks = data;  
    });
    
    route = "/get_user_wants/" + $scope.current_user_id;
    $http.get(route).success(function(data){
        $scope.my_wants = data;
    });
      
    route = "/get_user_breaks/" + $scope.current_user_id;
    $http.get(route).success(function(data){
        $scope.my_breaks = data;
    });
});


myApp.controller("scheduleCtrl", function($scope, $http){

    $scope.hours = 4;
    $scope.current_hours = $scope.hours;
     
    $scope.new_schedule = function(){
        var route = "/get_schedule/" + $scope.hours;
        $http.get(route).success(function(data){
            $scope.schedule = data;
            $scope.current_hours = $scope.hours;
        });
    };
    
    $scope.new_schedule();
     
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


myApp.controller("addTaskCtrl", function($scope, $http){

    $scope.validate = function(){
        if($scope.taskDescription == null || $scope.taskDescription == ""){
            alert("Please enter a description");
            return false;
        }
        if($scope.taskDueDate == null || $scope.taskDueDate == ""){
            alert("Please enter a due date");
            return false;
        }
        if($scope.taskType == null || $scope.taskType == ""){
            
            //TODO here : validate its one of the proper types?
            
            alert("Please enter a type");
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
            "task_description" : $scope.taskDescription, 
            "task_due_date" : $scope.taskDueDate,
            "task_type" : $scope.taskType
        };

        $http.get("/add_task_to_db", {params : parms}).success(function(data){
            alert("Task added!");
        });

    }

});


myApp.controller("addWantCtrl", function($scope, $http){

    $scope.validate = function(){
        if($scope.wantDescription == null || $scope.wantDescription == ""){
            alert("Please enter a description");
            return false;
        }
        if($scope.wantCategory == null || $scope.wantCategory == ""){
            alert("Please enter a Category");
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
            "want_description" : $scope.wantDescription, 
            "want_category" : $scope.wantCategory,
        };

        $http.get("/add_want_to_db", {params : parms}).success(function(data){
            alert("Want added!");
        });

    }

});


myApp.controller("addBreakCtrl", function($scope, $http){

    $scope.validate = function(){
        if($scope.breakDescription == null || $scope.breakDescription == ""){
            alert("Please enter a description");
            return false;

        }
        if($scope.breakurl == null || $scope.breakurl == ""){
            alert("Please enter url");
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
            "break_description" : $scope.breakDescription,
            "break_url" : $scope.breakurl,
        };

        $http.get("/add_break_to_db", {params : parms}).success(function(data){
            alert("break added!");
        });

    }

});
