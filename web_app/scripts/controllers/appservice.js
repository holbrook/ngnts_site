'use strict';

/**
 * @ngdoc function
 * @name ngntsAppApp.controller:BizServiceCtrl
 * @description
 * # BizServiceCtrl
 * Controller of the ngntsAppApp
 */
angular.module('ngntsApp')
  .controller('AppServiceCtrl', function ($scope, $routeParams) {
    console.log('AppServiceCtrl controller');
    $scope.code = $routeParams.code;
  });
