# The Manual

This is not a book about snapshots. This is a book about freedom.

Every system administrator knows the fear. The update that might break
everything. The configuration change that could bring down production. The
moment you type dnf update and wonder if you'll still have a working system in
ten minutes. We've all been there, finger hovering over Enter, mentally
rehearsing the recovery procedure.

It doesn't have to be this way.

Snapshot based rollback used to be the preserve of expensive enterprise
operating systems, storage arrays, and teams of specialists. The technology
existed, but it was locked away behind proprietary interfaces, complex
procedures, and eye-watering license fees. Ordinary administrators on ordinary
Linux systems were expected to make do with a bag of bits: hand-rolled
solutions, backups, prayers, and long nights.

The Manual exists because we believe everyone deserves a safety net. If you can
type a command, you can protect your system. If something goes wrong, you can
go back. It really is that simple.

This book will show you how to manage snapshots the easy way. Not just “the
enterprise way”. Not the "consult your storage administrator" way. The way that
lets you make changes with confidence, experiment without fear, and sleep
soundly knowing that yesterday's working system is only a reboot away.

You don't need expensive hardware. You don't need a team of experts. You need
Linux, some disk space, and the willingness to try.

The rest is just details. That's what this book is for.

Be ready to ride the big dipper of the mixed metaphor. Be ready to dip your
hands in the lucky bag of block devices, gather the storm clouds of entropy,
and anoint your own rollback strategy. Because it is only by following the
clear and concise instructions contained in this book that you can realize your
long held dream of running system updates without fear, thus guaranteeing your
place forever in the sacred annals of Uptime History.

One caveat before we begin: snapshots are not backups. They live on the same
storage as your data, and if that storage fails, your snapshots fail with it.
Nothing in this book replaces a tested backup strategy. But for the everyday
mishaps — the botched update, the configuration mistake, the accidental
deletion — snapshots will save you more times than you can count. Just
remember: backups will get you through times of no snapshots better than
snapshots will get you through times of no backups.
