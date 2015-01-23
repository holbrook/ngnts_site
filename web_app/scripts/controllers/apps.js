'use strict';

/**
 * @ngdoc function
 * @name ngntsApp.controller:AppsCtrl
 * @description
 * # AppsCtrl
 * Controller of the ngntsApp
 */
angular.module('ngntsApp')
  .controller('AppsCtrl', function ($scope) {
    var types = ['success', 'info', 'warning', 'danger'];
    $scope.stacked = [
        {value: 76, type: 'success', label:'已接入：299'},
        {value: 24, type: 'info', label:'未接入：77'},
    ];
  });
