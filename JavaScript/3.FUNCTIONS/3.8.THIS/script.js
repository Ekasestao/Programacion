var guide = {
    title: 'Guide to programming',
    content: 'Content will go here',
    visibleToUser: function(viewingUserRole) {
        if (viewingUserRole === 'paid') {
            return true;
        } else {
            return false;
        }
    },
    renderContent: function(UserRole) {
        if (this.visibleToUser(UserRole)) {
            console.log(this.title + ' - ' + this.content);
        } else {
            this.content = '';
            console.log(this.title + ' - ' + this.content)
        }
    }
}

user = { role: 'free'};
guide.renderContent(user.role);