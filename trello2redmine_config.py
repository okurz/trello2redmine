# -*- coding: utf-8 -*-

# This is the trello2redmine configuration file.
# All data here is exemplary, you need to fill it properly for the script to work!

# Trello configuration
trello_board_link = 'https://trello.com/b/nSONZFOR'	# As found on the board in Menu -> More -> Link to this board.

# Redmine configuration
redmine_root_url = 'https://progress.opensuse.org'
redmine_project_identifier = 'qam-qasle-collaboration'	# As appears in the Redmine URLs.
redmine_default_user = 'Oliver Kurz'			# Trello cards which are unassigned or whose assignee does not have a mapping in username_map will be assigned to this Redmine user.
redmine_verify_certificates = True			# Whether to verify SSL certificates.
redmine_api_key = ''				# Redmine REST API key. See: http://www.redmine.org/projects/redmine/wiki/Rest_api#Authentication

# Trello card label to Redmine priority map.
label_map = {
	u'':				u'Normal',	# Default for no label.
}

# Trello-to-Redmine username map. Both are displayed names, *not* logins or IDs! Redmine names are resolved to user IDs behind the scenes.
username_map = {
	u'okurz':		u'okurz',
	u'Foo Bar':			u'Foo Bar',
	u'Nickname':		u'Full Name',
}

# Trello list to Redmine status map. Redmine statuses are displayed names, *not* IDs! Statuses are resolved to IDs behind the scenes.
list_map = {
	u'TODO':				u'New',
	u'DOING':				u'In Progress',
	u'DONE':			u'Resolved',
	u'Standing topics / status quo updates':			u'Feedback',
}
