#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: mcxiaoke
# @Date:   2015-08-13 11:20:23

HEAD = u'''<!DOCTYPE html>
<html lang="zh_CN">
    <head>
        <title>$title</title>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style type="text/css">
            html,body,p {
                font-size: 100%;
                padding: 0;
                margin: 0;
            }
            body {
                background-color:#2183B4;
            }
            a img {
                border:none;
            }
            .header{
               margin:0px auto;
               padding:24px; 
               width:60%;
            }
            .header p{
                color:#ffffff;
                font-size:150%;
                text-align:center;
                margin:16px;
            }
            .footer{
                margin:0px auto;
                padding 8px;
                width:60%;
            }
            .footer p{
                color:#ffffff;
                font-size:50%;
                text-align:center;
                margin:16px;
            }
            .footer a{
                text-decoration: none;
                color:#ffffff;
            }
            .timeline2{
                 margin:0px auto;
                 width:640px;
                 background-color: #ffffff;
            }
            .status_box{
                margin:0px auto;
                width:660px;
                background-color: #ffffff;
                border-bottom:1px dashed #e0e0e0;
            }
            .status_box:hover { 
                background-color: #f6f6f6; 
            }
            .status {
                 margin:0px auto;
                 padding: 20px;
                 width:540px;
                 line-height:130%;
            }
            .st_text{
                color:#4B585D;
            }
            .st_photo{
                text-decoration: none;
                color: #3F9ECD;
                font-size:90%;
                margin-left:8px;
            }
            .st_meta{
                font-size: 80%;
                margin-bottom: 12px;
            }
            .st_name {
                color: #3F9ECD;
                font-weight: bold;
            }
            .st_uid {
                color: #999999;
            }
            .st_time:hover { 
                background-color:#3F9ECD;
                color:#ffffff;
            }
            .st_time{
                margin-left:16px;
                font-size: 70%;
                color:#999999;
                padding:2px;
                text-decoration: none;
                border-bottom:1px dashed #a0a0a0;
            }
        </style>
    </head>
'''

BODY_HEADER = u'''
    <body>
        <div class="header"><p>$title<p></div>
'''
BODY_FOOTER = u'''
        <div class="footer">
            <p id="copyright" class="copyright">Generated by 
                <a href="https://github.com/mcxiaoke/pyfanfou">PyFanfou</a>
            </p>
        </div>
    </body>
</html>
'''

STATUS_TEMPLATE = u'''
<div class="status_box">
    <div class="status" id="st_$id">
        <div class="st_meta">
            <span class="st_name">$name</span>
            <span class="st_uid">(@$uid)</span>
            <a class="st_time" href="http://fanfou.com/statuses/$id" 
            data-time="$raw_time" target="_blank">$time</a>
        </div>
        <span class="st_text">$text</span>
        <a class="st_photo" href="$photo_url" target="_blank">$photo_link</a>
    </div>
</div>
'''

MARKDOWN_HEADER = u'''
## $title

'''

MARKDOWN_FOOTER = u'''

Generated by [**pyfanfou**](https://github.com/mcxiaoke/pyfanfou)

'''

MARKDOWN_STATUS = u'''
- $text  $photo (*$time*) [>](http://fanfou.com/statuses/$id)

'''

TEXT_HEADER = u'''$title

'''

TEXT_FOOTER = u'''

Generated by https://github.com/mcxiaoke/pyfanfou
'''

TEXT_STATUS = u'''
$text ($time $id)
'''
