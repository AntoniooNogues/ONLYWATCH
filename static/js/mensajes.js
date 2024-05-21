// static/js/messages.js

function closeNotification(element) {
    const notification = element.closest('.notification');
    if (notification) {
        notification.remove();
    }
}

function bindNotificationEvents() {
    document.querySelectorAll('.notification .delete').forEach(button => {
        button.addEventListener('click', () => {
            closeNotification(button);
        });
    });
}

function autoDismissNotification(notification) {
    setTimeout(() => {
        notification.remove();
    }, 3500);
}

document.addEventListener('DOMContentLoaded', () => {
    bindNotificationEvents();

    // Auto-dismiss each notification individually
    document.querySelectorAll('.notification').forEach(notification => {
        autoDismissNotification(notification);
    });

    window.updateMessages = function(messages_Html) {
        const messagesContainer = document.getElementById('messages-container');
        messagesContainer.innerHTML = messages_Html;
        bindNotificationEvents();

        // Auto-dismiss each new notification individually
        document.querySelectorAll('.notification').forEach(notification => {
            autoDismissNotification(notification);
        });
    }
});