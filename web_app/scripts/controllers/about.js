'use strict';

/**
 * @ngdoc function
 * @name ngntsApp.controller:AboutCtrl
 * @description
 * # AboutCtrl
 * Controller of the ngntsApp
 */
angular.module('ngntsApp')
  .controller('AboutCtrl', function ($scope) {
    $scope.awesomeThings = [
      'HTML5 Boilerplate',
      'AngularJS',
      'Karma'
    ];

    $scope.oneAtATime = true;
  });
