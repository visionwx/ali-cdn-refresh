# ali-cdn-refresh

## Description
this action is used to trigger CDN refresh.

## Usage
```
- name: CDN Refresh
    uses: visionwx/ali-cdn-refresh@v1.0.0
    with:
        accessKeyId: ${{ secrets.ALIYUN_CDN_ACCESS_KEY_ID }}
        accessKeySecret: ${{ secrets.ALIYUN_CDN_ACCESS_KEY_SECRET }}
        type: Directory
        path: https://your.domain.com
```

## Inputs
- accessKeyId: the aliyun access key id with permission to manage CDN
- accessKeySecret: the aliyun access key secret with permission to manage CDN
- type: the refresh operation type, File or Directory
- path: the object path you want to refresh, e.g. https://your.domain.com/index.html, https://your.domain.com/