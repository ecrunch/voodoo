

myApp = angular.module("myApp", []);


myApp.controller("Main", function($scope){
    $scope.message = "Angular Works";   
})



myApp.controller("SchedulerCtrl", function($scope, $http){


    $scope.schedule = [];
    $scope.all_users = [];
    $scope.all_tasks = [];
    $scope.all_wants = [];
    $scope.all_breaks =[];
    
    $scope.hours = 4;

    $scope.selected_item = null;
    
    $scope.item_display = [];
    $scope.show_all_users = false;
    $scope.show_all_tasks = false;
    $scope.show_all_wants = false;
    $scope.show_all_breaks = false;
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
            $scope.show_all_tasks = false;
            $scope.show_item = false;
        });

    }


    $scope.display_all_users = function display_all_users(){
        
        var route = "/all_users";
        $http.get(route).success(function(data){
            $scope.all_users = data;
            $scope.show_all_users = true;
            $scope.show_all_tasks = false;
            $scope.show_all_wants = false;
            $scope.show_all_breaks = false;
            $scope.show_item = false;
        });
    }

    $scope.display_all_tasks = function display_all_tasks(){
        
        var route = "/all_tasks";
        $http.get(route).success(function(data){
            $scope.all_tasks = data;
            $scope.show_all_tasks = true;
            $scope.show_all_users = false;
            $scope.show_all_wants = false;
            $scope.show_all_breaks = false;
            $scope.show_item = false;
        });
    }

    $scope.display_all_wants = function display_all_wants(){
        
        var route = "/all_wants";
        $http.get(route).success(function(data){
            $scope.all_wants = data;
            $scope.show_all_wants = true;
            $scope.show_all_users = false;
            $scope.show_all_tasks = false;
            $scope.show_all_breaks = false;
            $scope.show_item = false;
        });
    }

    $scope.display_all_breaks = function display_all_breaks(){
        
        var route = "/all_breaks";
        $http.get(route).success(function(data){
            $scope.all_breaks = data;
            $scope.show_all_breaks = true;
            $scope.show_all_users = false;
            $scope.show_all_tasks = false;
            $scope.show_all_wants = false;
            $scope.show_item = false;
        });
    }
    
    $scope.display_item = function display_item(item){

        $scope.selected_item = item;
        
        //is a task
        if($scope.selected_item["class"] == "Task"){
         
            $scope.item_display = [
                {"field_name" : "Type", "field_value" : $scope.selected_item["class"]},
                {"field_name" : "Score", "field_value" : $scope.selected_item["score"]},
                {"field_name" : "Placement", "field_value" : $scope.selected_item["placement"]},
                {"field_name" : "Due Date", "field_value" : $scope.selected_item["due_date"]}
            ];
        }
        
        else{

            //is a want
            if($scope.selected_item["class"] == "Want"){ 
                $scope.item_display = [
                    {"field_name" : "Type", "field_value" : $scope.selected_item["class"]},
                    {"field_name" : "Category", "field_value" : $scope.selected_item["category"]}
                ];
            }  

            //is a break
            else{
                $scope.item_display = [
                    {"field_name" : "Type", "field_value" : $scope.selected_item["class"]},
                    {"field_name" : "URL", "field_value" : $scope.selected_item["url"]}
                ];
            }
        }

        $scope.show_item = true;
        $scope.show_all_users = false;
        $scope.show_all_tasks = false;
        $scope.show_all_wants = false;
        $scope.show_all_breaks = false;

    }


    $scope.finish_item = function finish_item(item){
   
        //alert(item.number);
         
    }

});



myApp.controller("InfoCtrl", function($scope, $http){


});






