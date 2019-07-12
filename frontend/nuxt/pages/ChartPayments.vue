<template>
  <v-card>
    <v-card-title>wykres</v-card-title>
    <v-card-text>
      <chartjs-line
        :backgroundcolor="bgColor"
        :beginzero="beginZero"
        :bind="true"
        :bordercolor="borderColor"
        :data="data[radio]"
        :datalabel="dataLabel"
        :labels="labels[radio]"
      />
    </v-card-text>
  </v-card>
</template>
<script>
export default {
  data() {
    return {
      bgColor: "#81894e",
      beginZero: true,
      borderColor: "#81894e",
      btn: [
        { label: "Today", value: "day" },
        { label: "This Week", value: "week" }
      ],
      data: {
        day: [1, 3, 5, 3, 1,25]
      },
      dataLabel: "Foo",
      labels: {
        day: [8, 10, 12, 14, 16, 18]
      },
      radio: "day"
    };
  }
}
</script>