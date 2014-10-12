

myApp = angular.module("myApp.controllers", []);



myApp.controller("mainCtrl", function($scope, $http, $location){
    
    
    /*
    *   TODO : get the user info from the db
    *   when logging in
    */
    
    $scope.current_user = "Zack";
    $scope.current_user_id = 1;
    $scope.userData = [];
    
    $scope.doneLoadingProfileData = false;


    $scope.userName = "";
    $scope.password = "";

    $scope.loggedIn = false;


    $scope.logIn = function(userName, password){
        
        var route = "/confirm_login";
        parms = {
            "userName": userName,
            "password": password
        }

        $http.get(route, {params: parms}).success(function(data){
            
            // We want to register the session with cookies or something
            // at this point
            
            if(data == 0){
                alert("Not a valid username/password");    
            } 
            else{
                $scope.loggedIn = true;
                $scope.loadProfile(data);
                $location.path("/home");
            }
        });
        
    };

    $scope.loadProfile = function(id){

        //run some validation checking on the id
        $scope.getUserData(id).then(function(res){    
            $scope.current_user_id = id;
            $scope.current_user = res["data"]["name"];
            $scope.userData = res["data"];
            $scope.doneLoadingProfileData = ! $scope.doneLoadingProfileData;
        });
    };
    
    $scope.getUserData = function(id){
        var route = "/get_user_data/" + id;
        return $http.get(route);
    };


    $scope.switchUser = function(id){
        $scope.loadProfile(id);
    }       

    $scope.loadProfile($scope.current_user_id);
    

});


myApp.controller("homeCtrl", function($scope, $http){

    $scope.bid = 1;
    $scope.wid = 1;
    $scope.tid = 1;
    $scope.cid = 1;

    $scope.delete_break = function(input){
        
        $scope.bid= input;
        alert($scope.bid);
        var route = "/delete_break_from_db/"+ $scope.bid;
        $http.get(route).success(function(data){
            alert("Success!");
        });
    };
    
    $scope.delete_want = function(input){
        
        $scope.wid= input;
        alert($scope.wid);
        var route = "/delete_want_from_db/"+ $scope.wid;
        $http.get(route).success(function(data){
            alert("Success!");
        });

    };

    $scope.delete_task = function(input){
          
        $scope.tid= input;
        alert($scope.tid);   
        var route = "/delete_task_from_db/"+ $scope.tid;
        $http.get(route).success(function(data){
            alert("Success!");
        });
    };
    
    
    $scope.delete_class = function(input){
    
        $scope.cid= input;
        alert($scope.cid);
        var route = "/delete_class_from_db/"+ $scope.cid;
        $http.get(route).success(function(data){
            alert("Success!");
        });
    };

        
    $scope.resetMinutes = function(task){
   
    
        var id = task.id;
       
        var parms = {
            "id": id
        };
       
        
        $http.get("/reset_minutes", {params: parms}).success(function(data){
            task.total_minutes = 0;
        });
         
    };


    $scope.$watch('doneLoadingProfileData', function(){

        $scope.my_classes = $scope.userData["classes"];
        $scope.my_tasks = $scope.userData["tasks"];
        $scope.my_wants = $scope.userData["wants"];
        $scope.my_breaks = $scope.userData["breaks"];

    });

});


myApp.controller("scheduleCtrl", function($scope, $http){

    $scope.hours = 4;
    $scope.current_hours = $scope.hours;
     
    $scope.new_schedule = function(){
        
        var route = "/get_schedule";
        
        var parms = {
            "hours": $scope.hours,
            "user_id": $scope.current_user_id
        };   
        
        $http.get(route, {params: parms}).success(function(data){
            $scope.schedule = data;
            $scope.current_hours = $scope.hours;
        });
    };
   
    
    $scope.logMinutes = function(id, minutes){
    
        var parms = {
            "id": id,
            "minutes": minutes   
        };
        $http.get("/log_minutes", {params: parms}).success(function(data){
            alert("New Total :  " + data["minutes"] + " minutes!");
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
