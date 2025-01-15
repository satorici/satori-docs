<script setup lang="ts">
import { useData } from 'vitepress'
import DefaultTheme from 'vitepress/theme'
import { provide } from 'vue'

const { isDark } = useData()

provide('toggle-appearance', async ({ clientX: x, clientY: y }: MouseEvent) => {
  isDark.value = !isDark.value;
  localStorage.setItem("theme", isDark.value ? "dark" : "light");
})

// Share theme between landing/dashboard
const savedTheme = localStorage.getItem('theme') ||
  (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
isDark.value = savedTheme === 'dark';
</script>

<template>
  <DefaultTheme.Layout />
</template>
