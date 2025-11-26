# YAML Post Schema

This document defines the structure for post YAML files.

## Common Fields

All post types share these common fields:

```yaml
id: unique-post-id
title: Post Title
content: |
  Multi-line content here.
  Supports markdown-style formatting.
author: Author Name
date: 2024-01-15
published: true
tags:
  - tag1
  - tag2
image: path/to/image.jpg  # Optional
```

## Post Types

### Event Posts (`data/events/`)

```yaml
id: event-001
type: event
title: Community Summer Festival
content: |
  Join us for the annual summer festival!
  Food, music, and fun for the whole family.
author: Event Committee
date: 2024-07-20
event_date: 2024-07-25
event_time: "14:00"
event_location: Community Center
published: true
tags:
  - festival
  - community
image: events/summer-festival.jpg
```

### General Information Posts (`data/info/`)

```yaml
id: info-001
type: info
title: Road Closure Notice
content: |
  Main street will be closed for maintenance
  from Monday to Wednesday next week.
author: Local Council
date: 2024-01-15
published: true
tags:
  - announcement
  - roadworks
expires: 2024-01-25  # Optional expiration date
```

### Advertisement Posts (`data/ads/`)

```yaml
id: ad-001
type: ad
title: Fresh Bread Daily
content: |
  Visit our bakery for fresh bread baked daily.
  Open 7am - 6pm Monday to Saturday.
author: Eikefjord Bakery
date: 2024-01-15
published: true
tags:
  - business
  - food
contact:
  phone: "+47 123 45 678"
  email: "bakery@example.com"
  website: "https://example.com"
image: ads/bakery.jpg
expires: 2024-12-31  # Optional expiration date
```

## File Naming Convention

- Events: `event-YYYY-MM-DD-slug.yaml` or `event-001.yaml`
- Info: `info-YYYY-MM-DD-slug.yaml` or `info-001.yaml`
- Ads: `ad-YYYY-MM-DD-slug.yaml` or `ad-001.yaml`

## Notes

- All dates in ISO format: `YYYY-MM-DD`
- Content supports multi-line text
- `published: false` posts are excluded from build
- Expired posts (if `expires` field exists and date passed) are excluded
