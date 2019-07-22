<template>
  <v-app>
    <SnackbarSuccess />
    <SnackbarError />
    <SnackbarInfo />
    <v-navigation-drawer
      v-model="drawer"
      :mini-variant="miniVariant"
      :clipped="clipped"
      fixed
      app
    >

  <v-list dense>
        <template v-for="(item, i) in items">
          <v-list-group
            v-if="item.children"
            :key="i"
            :to="item.to"
            router
            exact
          >
            <template v-slot:activator>
              <v-list-tile>
              <v-list-tile-action>
                <v-icon>{{ item.icon }}</v-icon>
              </v-list-tile-action>
                <v-list-tile-content>
                  <v-list-tile-title>
                    {{ item.title }}
                  </v-list-tile-title>
                </v-list-tile-content>
              </v-list-tile>
            </template>
            <v-list-tile
              v-for="(child, i) in item.children"
              :key="i"
              :to="child.to"
              router
              exact
              >
              <v-list-tile-action>
                <v-icon>{{ child.icon }}</v-icon>
              </v-list-tile-action>
              <v-list-tile-content>
                <v-list-tile-title>
                  {{ child.title }}
                </v-list-tile-title>
              </v-list-tile-content>
            </v-list-tile>
          </v-list-group>
          <v-list-tile v-else :key="item.title" :to="item.to"
            router
            exact>
            <v-list-tile-action>
              <v-icon>{{ item.icon }}</v-icon>
            </v-list-tile-action>
            <v-list-tile-content>
              <v-list-tile-title>
                {{ item.title }}
              </v-list-tile-title>
            </v-list-tile-content>
          </v-list-tile>
        </template>
      </v-list>

    </v-navigation-drawer>
    <v-toolbar
      :clipped-left="clipped"
      fixed
      app
    >
      <v-toolbar-side-icon @click="drawer = !drawer" />
      <v-btn
        icon
        @click.stop="miniVariant = !miniVariant"
      >
        <v-icon>{{ `chevron_${miniVariant ? 'right' : 'left'}` }}</v-icon>
      </v-btn>
      <v-btn
        icon
        @click.stop="clipped = !clipped"
      >
        <v-icon>web</v-icon>
      </v-btn>
      <v-btn
        icon
        @click.stop="fixed = !fixed"
      >
        <v-icon>remove</v-icon>
      </v-btn>
      <v-toolbar-title v-text="title" class="light-blue--text darken-4--text" />
      <v-spacer />
      <v-btn
        icon
        @click.stop="rightDrawer = !rightDrawer"
      >
        <v-icon>menu</v-icon>
      </v-btn>
    </v-toolbar>
    <v-content>
      <v-container>
        <nuxt />
      </v-container>
    </v-content>
    <v-navigation-drawer
      v-model="rightDrawer"
      :right="right"
      temporary
      fixed
    >
      <v-layout row wrap align-center justify-center text-xs-center>
        <v-sheet
              class="d-flex"
              color="blue-grey lighten-4"
              width="100%"
            >
        <v-flex xs3></v-flex>
        <v-flex xs2>
           <v-btn 
           flat
            fab
            small
            icon
            @click="switchLang('pl')">
            <img src="~/static/flags/pl.svg" alt="pl" width='20'>
            </v-btn>
        </v-flex>
        <v-flex xs2>
          <v-btn 
           flat
            fab
            small
            icon
            @click="switchLang('en')">
            <img src="~/static/flags/en.svg" alt="en" width='20'>
            </v-btn>
        </v-flex>
        <v-flex xs2>
          <v-btn 
           flat
            fab
            small
            icon
            @click="switchLang('de')">
            <img src="~/static/flags/de.svg" alt="de" width='20'>
            </v-btn>
        </v-flex>
        <v-flex xs3 text-xs-right>
          <v-btn
            flat
            fab
            small
            icon>
            <v-icon @click.native="right = !right" light>compare_arrows</v-icon>
          </v-btn>
        </v-flex>
        </v-sheet>
      </v-layout>
    </v-navigation-drawer>
  </v-app>
</template>

<script>
import SnackbarSuccess from '~/components/SnackBarSuccess'
import SnackbarError from '~/components/SnackBarError'
import SnackbarInfo from '~/components/SnackBarInfo'

export default {
  components: {
      SnackbarSuccess,
      SnackbarError,
      SnackbarInfo
  },
  data() {
    return {
      clipped: true,
      drawer: true,
      fixed: false,
      items: [
        {
          icon: 'dashboard',
          title: 'Dashboard',
          to: '/'
        },
        {
          icon: 'attach_money',
          title: this.$t('navigation.paymentsList'),
          to: '/FeeList'
        },
        {
          icon: 'list',
          title: this.$t('navigation.players'),
          to: '/MainList'
        },
        {
          icon: 'bar_chart',
          title: this.$t('navigation.charts'),
          children: [
            {
              title: this.$t('navigation.payments'),
              to: '/ChartPayments'
            }
          ]
        }
      ],
      miniVariant: false,
      right: true,
      rightDrawer: false,
      title: this.$t('title')
    }
  },
  methods: {
    switchLang(lang) {
       this.$i18n.setLocaleCookie(lang)
       window.location.reload(true)
    }
  },
  mounted() {}
}
</script>
