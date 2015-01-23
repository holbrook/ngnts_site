'use strict';

/**
 * @ngdoc function
 * @name ngntsApp.controller:MsgListCtrl
 * @description
 * # MsgListCtrl
 * Controller of the ngntsApp
 */
angular.module('ngntsApp')
  .controller('MsgListCtrl', function ($scope, $rootScope, $http) {
    console.log("msgList controller");
    $scope.messages = $rootScope.idx;

  });
