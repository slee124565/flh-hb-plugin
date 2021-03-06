'use strict';

/**
 * @ngdoc service
 * @name homeboxApp.SettingsService
 * @description
 * # SettingsService
 * Service in the homeboxApp.
 */
angular.module('homeboxApp')
  .constant('apiBaseURL', '/')
  .service('SettingsService', ['$http','apiBaseURL', 
    function ($http, apiBaseURL) {
        
        this.getSiteConfig = function() {
            return $http.get(apiBaseURL + 'webapp/api/config');
        };
        
        this.setSiteConfig = function(newConfig) {
            return $http({
                method: 'POST',
                url: apiBaseURL + 'webapp/api/config',
                data: newConfig,
            });
        };
        
        this.factoryReset = function() {
            return $http({
                method: 'POST',
                url: apiBaseURL + 'webapp/api/reset',
                data: {token:'flhomebox'},
            });
        };
  }]);
