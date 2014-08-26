

myApp = angular.module("myApp.controllers", []);


myApp.controller("Main", function($scope){
    $scope.message = "Angular Works";   
});



myApp.controller("SchedulerCtrl", 

["$scope", "$http", "ScheduleManager", "SelectedItemManager", 

function($scope, $http, ScheduleManager, SelectedItemManager){

    $scope.hours = 4;
     
    ScheduleManager.newSchedule($scope.hours)
    .success(function(data){
        $scope.schedule = data;
        $scope.header_hour= $scope.hours;
    });
   
    $scope.all_users = [];
    $scope.all_tasks = [];
    $scope.all_wants = [];
    $scope.all_breaks =[];
    

    $scope.selected_item = null;
    
    $scope.item_display = [];
    $scope.show_all_users = false;
    $scope.show_all_tasks = false;
    $scope.show_all_wants = false;
    $scope.show_all_breaks = false;
    $scope.show_item = false;
   
    $scope.is_task = false; 


    $scope.test = function(){
        SelectedItemManager.test();
    }


    $scope.update_schedule = function update_schedule(){
        ScheduleManager.newSchedule($scope.hours)
        .success(function(data){
            $scope.schedule = data;
            $scope.header_hour= $scope.hours;
            $scope.show_item = false;
        });
    }


    $scope.get_all = function get_all(route){
        return $http.get(route);
    }



    $scope.display_all_users = function display_all_users(){
        
        var route = "/all_users";
        $scope.get_all(route).success(function(data){
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
            $scope.item_display = SelectedItemManager.formatTask($scope.selected_item);
            $scope.is_task = true;
        }
        
        else{
            //is a want
            if($scope.selected_item["class"] == "Want"){ 
                $scope.item_display = SelectedItemManager.formatWant($scope.selected_item);
            }  

            //is a break
            else{
                $scope.item_display = SelectedItemManager.formatBreak($scope.selected_item);
            }

            $scope.is_task = false;
        }

        $scope.show_item = true;
        $scope.show_all_users = false;
        $scope.show_all_tasks = false;
        $scope.show_all_wants = false;
        $scope.show_all_breaks = false;

    }


    $scope.add_time = function add_time(slot){
       
        var id = slot["item"].id; 
        var time_slot = slot["timeslot"];
        var description = slot["item"].description;
        var item_class = slot["item"].class;
      
                       
        ScheduleManager.addTime(id, time_slot, item_class)
        .success(function(data){

            slot["item"].total_minutes = data["minutes"];
            if($scope.show_item){
                $scope.display_item(slot["item"]);
            }
            
            //figure out a better way than 
            //reloading the element
            $scope.get_all("/all_tasks").success(function(data){
                $scope.all_tasks = data;  
            });
        });
    }

    $scope.reset_minutes = function resetMinutes(item){

        var id = item.id;
        var item_class = item.class;

        ScheduleManager.resetTime(id, item_class)
        .success(function(data){
            
            //clears inside item display
            item.total_minutes = 0;
           
            //need to find the corresponding task in the schedule and
            //set it to zero minutes 
            var length = $scope.schedule.length;
            var element = null;
            
            //for each(slot in $scope.schedule){
            for(var i = 0; i < length; i++){
            
                if($scope.schedule[i]["item"].id == item.id && $scope.schedule[i]["item"].class == item.class){
                    $scope.selected_item = $scope.schedule[i]["item"];
                    $scope.selected_item["total_minutes"] = 0;
                    break;
                }
            }
            if($scope.show_item){
                $scope.display_item($scope.selected_item);
            }
        });



    } 


}]);



myApp.controller("InfoCtrl", function($scope, $http){


});






