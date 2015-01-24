'use strict';

/**
 * @ngdoc overview
 * @name ngntsApp
 * @description
 * # ngntsApp
 *
 * Main module of the application.
 */
var myApp = angular.module('ngntsApp', [
    'ngAnimate',
    'ngCookies',
    'ngResource',
    'ngRoute',
    'ngSanitize',
    'ngTouch',
    'ui.bootstrap'
    // 'angular-jqcloud'
  ]);


myApp.run(function ($rootScope, $http){
    console.log('app run');
    $http({url:'data/index.json'})
      .success(function(data){
          $rootScope.idx = data;
          // alert($rootScope.idx.messages['110002'].code);
      })
      .error(function(status){
          alert(status);
      });

  });

myApp.config( function($routeProvider) {
    console.log('app config');
    $routeProvider
      .when('/', {
        templateUrl: 'views/main.html',
        controller: 'MainCtrl'
      })
      .when('/bizservice/:code', {
        templateUrl: 'views/bizservice.html',
        controller: 'BizServiceCtrl'
      })
      .when('/appservice/:code', {
        templateUrl: 'views/appservice.html',
        controller: 'AppServiceCtrl'
      })
      .when('/message', {
        templateUrl: 'views/msg_list.html',
        controller: 'MsgListCtrl'
      })
      .when('/message/:code', {
        templateUrl: 'views/message.html',
        controller: 'MsgDetailCtrl'
      })
      .when('/scopes', {
        templateUrl: 'views/scope_list.html',
        controller: 'ScopeListCtrl'
      })
      .when('/scopes/:scope', {
        templateUrl: 'views/scope_detail.html',
        controller: 'ScopeDetailCtrl'
      })
      .when('/applications', {
        templateUrl: 'views/apps.html',
        controller: 'AppsCtrl'
      })
      .when('/dict', {
        templateUrl: 'views/dict.html',
        controller: 'DictCtrl'
      })
      .when('/tools', {
        templateUrl: 'views/tools.html',
        controller: 'ToolsCtrl'
      })
      .when('/about', {
        templateUrl: 'views/about.html',
        controller: 'AboutCtrl'
      })

      .otherwise({
        redirectTo: '/'
      });
});

myApp.controller('myCtrl', function() {
    console.log('app controller');
});








