function applicationTA () {

    var makeGetRequest = function(url, onSuccess, onFailure) {
        $.ajax({
            type: 'GET',
            url: apiUrl + url,
            dataType: "json",
            success: onSuccess,
            error: onFailure
        });
    };

    var makePostRequest = function(url, data, onSuccess, onFailure) {
        $.ajax({
            type: 'POST',
            url: apiUrl + url,
            data: JSON.stringify(data),
            contentType: "application/json",
            dataType: "json",
            success: onSuccess,
            error: onFailure
        });
    };

    var login = function() {
        alert("logged in");
    }

    var createAccount = function() {
        alert("created account");
    }

    var start = function() {
        $("#login").click(function() {
            login();
        });
        $("#create-account").click(function() {
            createAccount();
        });
    };

    return {
        start: start
    };
    
};