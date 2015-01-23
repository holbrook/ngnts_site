'use strict';

/**
 * @ngdoc function
 * @name ngntsAppApp.controller:DictCtrl
 * @description
 * # DictCtrl
 * Controller of the ngntsAppApp
 */
angular.module('ngntsApp')
  .controller('DictCtrl', function ($scope, $rootScope) {
    console.log("DictCtrl controller");
    $scope.messages = $rootScope.idx;
  });
