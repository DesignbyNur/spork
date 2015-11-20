#!/bin/bash

  wp menu list
  wp post create --post_type='page' --post_title='home' --post_status=Published license.txt 
  wp post create --post_type='page' --post_title='about-us' --post_status=Published license.txt 
  wp post create --post_type='page' --post_title='contact'  --post_status=Published license.txt 
  wp post create --post_type='page' --post_title='blog' --post_status=Published  license.txt 
  wp post create --post_type='page' --post_title='gallery' --post_status=Published  license.txt 
  wp menu create top-menu
  wp menu location assign top-menu primary
  wp menu list
  for i in `wp post list --post_type='page' --format=ids`
	do
	wp menu item add-post top-menu $i
	done

  wp menu list
