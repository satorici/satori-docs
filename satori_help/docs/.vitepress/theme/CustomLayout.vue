<script setup lang="ts">
import { useData } from 'vitepress'
import DefaultTheme from 'vitepress/theme'
import { provide } from 'vue'

const { isDark } = useData()

function getCookie(name) {
  const value = `; ${document.cookie}`;
  const parts = value.split(`; ${name}=`);
  if (parts.length === 2) return parts.pop().split(';').shift();
}

function setCookie(name, value) {
  let date = new Date();
  date.setTime(date.getTime() + (365 * 24 * 60 * 60 * 1000));
  let expires = "; expires=" + date.toUTCString();
  document.cookie = name + "=" + (value || "") + expires + "; path=/; domain=.satori.ci";
}

provide('toggle-appearance', async ({ clientX: x, clientY: y }: MouseEvent) => {
  isDark.value = !isDark.value;
  // Save in a cookie to share the theme between subdomains
  setCookie("theme", isDark.value ? "dark" : "light");
})

// Share theme between landing/dashboard
const savedTheme = getCookie('theme') ||
  (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
isDark.value = savedTheme === 'dark';
</script>

<template>
  <DefaultTheme.Layout />
</template>
