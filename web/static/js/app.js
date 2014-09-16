

angular.module('myApp', [ 
    'myApp.controllers',
    'myApp.services',
    'myApp.directives',
    'ngRoute',
    'route-segment',
    'view-segment'
])
.config(function($routeSegmentProvider, $routeProvider){

    $routeSegmentProvider.
    
    when('/home', 's1').
    when('/schedule', 's2').
    when('/add', 's3').
    when('/add/class', 's3.addClass').
    when('/add/task', 's3.addTask').
    when('/add/break', 's3.addBreak').
    when('/add/want', 's3.addWant').

    segment('s1', {
        templateUrl: 'static/partials/home.html',
        controller: 'homeCtrl'
    }).
    segment('s2', {
        templateUrl: 'static/partials/schedule.html',
        controller: 'scheduleCtrl'
    }).
    segment('s3', {
        templateUrl: 'static/partials/add.html'        
    }).
    within().
        segment('addClass', {
            templateUrl: 'static/partials/add_class.html',
            controller: 'addClassCtrl'
        }).
        segment('addTask', {
            templateUrl: 'static/partials/add_task.html',
            controller: 'addTaskCtrl'
        }).
        segment('addBreak', {
            templateUrl: 'static/partials/add_break.html',
            controller: 'addBreakCtrl'
        }).
        segment('addWant', {
            templateUrl: 'static/partials/add_want.html',
            controller: 'addWantCtrl'
        }).
        up();

    $routeProvider.otherwise({
        redirectTo: '/home'
    });


});


