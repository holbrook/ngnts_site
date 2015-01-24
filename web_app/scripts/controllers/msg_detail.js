'use strict';

/**
 * @ngdoc function
 * @name ngntsApp.controller:MessageCtrl
 * @description
 * # MessageCtrl
 * Controller of the ngntsApp
 */
angular.module('ngntsApp')
  .controller('MsgDetailCtrl', function ($scope, $routeParams, $http) {
    console.log('msgDetail controller');
    $scope.code = $routeParams.code;

    $http({url:'data/messages/'+$scope.code+'.json'})
      .success(function(data){
          $scope.message = data;
          for(var x in $scope.message.request){
            var item = $scope.message.request[x];
            if (item.type.indexOf('N') >= 0){
              if (item.type.indexOf('.') >=0 ){
                item.rideType = 'Doub';
              }
              else{
               item.rideType = 'Int';
              }
            }else{
              if (item.rideType === 'C1'){
                item.rideType = 'Char';
              }
              else{
                item.rideType = 'Str';
              }
            }
          }
      });
  });
