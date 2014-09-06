

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
        up();

    $routeProvider.otherwise({
        redirectTo: '/home'
    });


});


