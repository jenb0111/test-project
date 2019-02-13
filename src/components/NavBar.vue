<template>
    <nav>
        <v-toolbar app>
            <v-toolbar-side-icon @click="drawer = !drawer"></v-toolbar-side-icon>
            <v-toolbar-title>
                <span class="font-weight-light">Tool</span>
                <span>bar</span>
            </v-toolbar-title>
            <v-spacer></v-spacer>
            <v-btn flat>
                <span>Sign Out</span>
                <v-icon>exit_to_app</v-icon>
            </v-btn>
        </v-toolbar>

        <v-navigation-drawer app v-model="drawer" class="pink">
            <v-list>
                <v-list-tile v-for="link in links" :key="link.text" router :to="link.route">
                    <v-list-tile-action>
                        <v-icon class="white--text">{{ link.icon }}</v-icon>
                    </v-list-tile-action>
                    <v-list-tile-content>
                        <v-list-tile-title class="white--text">{{ link.text }}</v-list-tile-title>
                    </v-list-tile-content>
                </v-list-tile>
            </v-list>
        </v-navigation-drawer>

    </nav>
</template>


<script>
export default {
    data() {
        return {
            drawer: false,
            links: [
                { icon: 'home', text: 'Home', route: '/' },
                { icon: 'folder', text: 'My projects', route: '/projects' },
                { icon: 'person', text: 'Teams', route: '/teams' }
            ]
        }
    }

}
</script>