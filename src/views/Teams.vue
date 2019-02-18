<template>
  <div class="teams">
    <h1>Hello!! There are teams.</h1>
    <v-container class="my-5">
      <!-- grid system -->
      <v-layout row wrap>
        <v-flex xs12 md6>
          <v-btn outline block>1</v-btn>
        </v-flex>
        <v-flex xs4 md6>
          <v-btn outline block>2</v-btn>
        </v-flex>
        <v-flex xs4 md6>
          <v-btn outline block>2</v-btn>
        </v-flex>
        <v-flex xs4 md6>
          <v-btn outline block>2</v-btn>
        </v-flex>
      </v-layout>

      <v-layout row wrap justify-space-around>
        <v-flex xs4 md3>
          <v-btn outline block class="success">1</v-btn>
        </v-flex>
        <v-flex xs4 md3>
          <v-btn outline block>1</v-btn>
        </v-flex>
      </v-layout>

      <v-tooltip bottom>
        <v-btn slot="activator" color="primary" dark>Button</v-btn>
        <span>tooltip</span>
      </v-tooltip>

      <v-layout row class="my-5">
        <v-tooltip top>
          <v-btn small flat color="grey" @click="sortBy('title')" slot="activator">
            <v-icon left small>folder</v-icon>
            <span class="caption text-lowercase">By project name</span>
          </v-btn>
          <span>Sort by project name</span>
        </v-tooltip>
        <v-tooltip top>
          <v-btn small flat color="grey" @click="sortBy('person')" slot="activator">
            <v-icon left small>person</v-icon>
            <span class="caption text-lowercase">By person</span>
          </v-btn>
          <span>Sort by person</span>
        </v-tooltip>
      </v-layout>

      <v-card flat class="pa-3" v-for="project in projects" :key="project.tile">
        <v-layout row wrap :class="`pa-3 project ${project.status}`">
          <v-flex xs12 md5>
            <div class="caption grey--text">Project title</div>
            <div>{{ project.title }}</div>
          </v-flex>
          <v-flex xs6 sm4 md2>
            <div class="caption grey--text">Person</div>
            <div>{{ project.person }}</div>
          </v-flex>
          <v-flex xs6 sm4 md2>
            <div class="caption grey--text">Due by</div>
            <div>{{ project.duedate }}</div>
          </v-flex>
          <v-flex xs6 sm4 md2>
            <div class="caption grey--text">Status</div>
            <div>
              <v-chip
                small
                :class="`${project.status} white--text caption my-2`"
              >{{ project.status }}</v-chip>
            </div>
          </v-flex>
        </v-layout>
        <v-divider></v-divider>
      </v-card>

      <v-card flat class="pa-3">
        <v-layout row wrap>
          <v-flex xs12 md5>
            <div class="caption grey--text">Project title</div>
            <div>Create a new website</div>
          </v-flex>
          <v-flex xs6 sm4 md2>
            <div class="caption grey--text">Person</div>
            <div>Plaifah Atthapaibul</div>
          </v-flex>
          <v-flex xs6 sm4 md2>
            <div class="caption grey--text">Due by</div>
            <div>Jan 1st, 2019</div>
          </v-flex>
          <v-flex xs6 sm4 md2>
            <div class="caption grey--text">Status</div>
            <div>Ongoing</div>
          </v-flex>
        </v-layout>
      </v-card>

      <v-layout row wrap>
        <v-flex xs12 sn6 md4 lg3 v-for="person in team" :key="person.name">
          <v-card flat class="text-xs-center ma-3">
            <v-responsive class="pt-4">
              <v-avatar size="100" class="grey lighten-2">
                <img :src="person.avatar">
              </v-avatar>
            </v-responsive>
            <v-card-text>
              <div class="subheading">{{ person.name }}</div>
              <div class="grey--text">{{ person.role }}</div>
            </v-card-text>
            <v-card-actions>
              <v-btn flat color="grey">
                <v-icon small left>message</v-icon>
                <span>Message</span>
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-flex>
      </v-layout>
    </v-container>
  </div>
</template>

<script>
import db from '@/fb'

export default {
  data() {
    return {
      projects: [
        // {
        //   title: "Design a new website",
        //   person: "Plaifah Atthapaibul",
        //   duedate: "Jan 11th, 2019",
        //   status: "ongoing",
        //   content:
        //     "Lorem ipsum dolor sit amet consectetur adipisicing elit. Eveniet ipsam voluptatibus harum aspernatur saepe quod minima quibusdam voluptate corporis asperiores consectetur vero assumenda blanditiis possimus veniam officia, odio aut consequuntur."
        // },
        // {
        //   title: "Coding",
        //   person: "Do Minjun",
        //   duedate: "Jan 1st, 2019",
        //   status: "complete",
        //   content:
        //     "Lorem ipsum dolor sit amet consectetur adipisicing elit. Eveniet ipsam voluptatibus harum aspernatur saepe quod minima quibusdam voluptate corporis asperiores consectetur vero assumenda blanditiis possimus veniam officia, odio aut consequuntur."
        // },
        // {
        //   title: "Design xxx",
        //   person: "Natcha Likitrungsan",
        //   duedate: "March 8th, 2019",
        //   status: "complete",
        //   contend:
        //     "Lorem ipsum dolor sit amet consectetur adipisicing elit. Eveniet ipsam voluptatibus harum aspernatur saepe quod minima quibusdam voluptate corporis asperiores consectetur vero assumenda blanditiis possimus veniam officia, odio aut consequuntur."
        // },
        // {
        //   title: "Create a community forum",
        //   person: "Im Jaebum",
        //   duedate: "Jan 6th, 2019",
        //   status: "overdue",
        //   content:
        //     "Lorem ipsum dolor sit amet consectetur adipisicing elit. Eveniet ipsam voluptatibus harum aspernatur saepe quod minima quibusdam voluptate corporis asperiores consectetur vero assumenda blanditiis possimus veniam officia, odio aut consequuntur."
        // }
      ],
      team: [
        { name: 'Plaifah Atthapaibul', role: 'Network Engineer', avatar: '/127859.jpg' },
        { name: 'Do Minjun', role: 'Developer', avatar: '/127860.jpg'},
        { name: 'Natcha Likitrungsan', role: 'Designer', avatar: '/127861.jpg' },
        { name: 'Im Jaebum', role: 'Sales Promotion', avatar: '/127862.jpg' }
      ]
    };
  },
  methods: {
    sortBy(prop) {
      this.projects.sort((a, b) => (a[prop] < b[prop] ? -1 : 1));
    }
  },
  created() {
    db.collection('projects').onSnapshot(res => {
      const changes = res.docChanges()
      changes.forEach(change => {
        if (change.type === 'added') {
          this.projects.push({
            ...change.doc.data(),
            id: change.doc.id
          })
        }
      })
    })
  }
};
</script>

<style>
.project.complete {
  border-left: 4px solid #3cd1c2;
}
.project.ongoing {
  border-left: 4px solid orange;
}
.project.overdue {
  border-left: 4px solid tomato;
}
.v-chip.complete {
  background: #3cd1c2;
}
.v-chip.ongoing {
  background: orange;
}
.v-chip.overdue {
  background: tomato;
}
</style>

