'use strict';

/**
 * @ngdoc function
 * @name ngntsAppApp.controller:BizServiceCtrl
 * @description
 * # BizServiceCtrl
 * Controller of the ngntsAppApp
 */
angular.module('ngntsApp')
  .controller('BizServiceCtrl', function ($scope, $routeParams) {
    console.log('BizServiceCtrl controller');
    $scope.code = $routeParams.code;
  });
