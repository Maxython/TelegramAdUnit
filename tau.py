from selenium import webdriver
import telebot
from telebot import types
from time import sleep

def google_adsense(bot, message_id, driver, url, id_iframe, time_sleep, words,view=None):
	"Sends ad units from Google AdSense"
	try:
		words['publication'] = False
		driver.set_window_size(1500, 800)
		driver.get(url)
		sleep(time_sleep)
		au = driver.find_element_by_id(id_iframe)
		driver.switch_to.frame(au)
		try:
			img = driver.find_element_by_tag_name('img')
			if 'https://tpc.googlesyndication.com/simgad/' in img.get_attribute('src'):
				img_src = img.get_attribute('src')
			else:
				img_src = None
		except Exception:
			img_src = None
		href = driver.find_elements_by_tag_name('a')
		for i in href:
			if 'https://adssettings.google.com/whythisad' in i.get_attribute('href'):
				url_google = i.get_attribute('href')
				break
			else:
				continue
		for i in href:
			if ('https://googleads.g.doubleclick.net/aclk' in i.get_attribute('href')) or ('https://www.googleadservices.com/pagead/aclk' in i.get_attribute('href')):
				href_url = i.get_attribute('href')
				break
			else:
				continue
		try:
			text_Body = driver.find_element_by_css_selector('div.body a').text
		except Exception:
			text_Body = None
		driver.quit()
		if img_src != None:
			textBody = '%s\n<a href="%s">%s</a>\n<a href="%s">%s</a>\nGoogle AdSense' % (words['text_ad'],url,words['you_site'],url_google,words['service_google'])
		else:
			textBody = '<a href="%s">%s</a>\n<a href="%s">%s</a>\n<a href="%s">%s</a>\nGoogle AdSense' % (href_url,words['text_ad'],url,words['you_site'],url_google,words['service_google'])
		if text_Body != None:
			textBody = textBody + '\n\n' + text_Body
		if view == None:
			mar = types.InlineKeyboardMarkup(row_width=1)
			but = types.InlineKeyboardButton(words['button_text'],url=href_url)
			mar.add(but)
			try:
				bot.send_photo(message_id, img_src, textBody, reply_markup=mar, parse_mode='html')
			except Exception:
				bot.send_message(message_id, textBody, reply_markup=mar, parse_mode='html')
			words['publication'] = True
		elif view == 'push-button':
			mar = types.InlineKeyboardMarkup(row_width=1)
			but = types.InlineKeyboardButton(words['button_text'],url=href_url,callback_data='onpress=True')
			mar.add(but)
			textBody = textBody + '\n\n' + words['push_text']
			try:
				bot.send_photo(message_id, img_src, textBody, reply_markup=mar, parse_mode='html')
			except Exception:
				bot.send_message(message_id, textBody, reply_markup=mar, parse_mode='html')
			words['publication'] = True
	except Exception as e:
		try:
			driver.quit()
		except Exception:
			pass

def yandex_ad_network(bot, message_id, driver, url, id_div, time_sleep, words,view=None):
	"Sends ad units from the Yandex ad network"
	try:
		id_split = id_div.split('_')
		id_yatag = 'ya_partner_'+id_split[len(id_split)-1]
		words['publication'] = False
		driver.set_window_size(1500, 800)
		driver.get(url)
		sleep(time_sleep)
		au = driver.find_elements_by_css_selector('yatag#%s iframe' % (id_yatag))[0]
		driver.switch_to.frame(au)
		a = driver.find_element_by_tag_name('a')
		a_href = a.get_attribute('href')
		img = driver.find_element_by_tag_name('img')
		img_src = img.get_attribute('src')
		driver.quit()
		textBody = '%s\n<a href="%s">%s</a>\n<a href="%s">%s</a>\nYandex Direct' % (words['text_ad'], url, words['you_site'], 'https://direct.yandex.ru/?partner', words['service_yandex'])
		if view == None:
			mar = types.InlineKeyboardMarkup(row_width=1)
			but = types.InlineKeyboardButton(words['button_text'],url=a_href)
			mar.add(but)
			try:
				bot.send_photo(message_id, img_src, textBody, reply_markup=mar, parse_mode='html')
			except Exception:
				bot.send_message(message_id, textBody, reply_markup=mar, parse_mode='html')
			words['publication'] = True
		elif view == 'push-button':
			mar = types.InlineKeyboardMarkup(row_width=1)
			but = types.InlineKeyboardButton(words['button_text'],url=a_href,callback_data='onpress=True')
			mar.add(but)
			textBody = textBody + '\n\n' + words['push_text']
			try:
				bot.send_photo(message_id, img_src, textBody, reply_markup=mar, parse_mode='html')
			except Exception:
				bot.send_message(message_id, textBody, reply_markup=mar, parse_mode='html')
			words['publication'] = True
	except Exception:
		try:
			a = driver.find_elements_by_xpath("//div[@id='%s']//a" % (id_div))
			for i in a:
				try:
					if 'https://an.yandex.ru/count/' in i.get_attribute('href'):
						a_href = i.get_attribute('href')
						break
				except Exception:
					continue
			driver.quit()
			textBody = '<a href="%s">%s</a>\n<a href="%s">%s</a>\n<a href="%s">%s</a>\nYandex Direct' % (a_href, words['text_ad'], url, words['you_site'], 'https://direct.yandex.ru/?partner', words['service_yandex'])
			if view == None:
				mar = types.InlineKeyboardMarkup(row_width=1)
				but = types.InlineKeyboardButton(words['button_text'],url=a_href)
				mar.add(but)
				bot.send_message(message_id, textBody, reply_markup=mar, parse_mode='html')
				words['publication'] = True
			elif view == 'push-button':
				mar = types.InlineKeyboardMarkup(row_width=1)
				but = types.InlineKeyboardButton(words['button_text'],url=a_href,callback_data='onpress=True')
				mar.add(but)
				textBody = textBody + '\n\n' + words['push_text']
				bot.send_message(message_id, textBody, reply_markup=mar, parse_mode='html')
				words['publication'] = True
		except Exception:
			try:
				driver.quit()
			except Exception:
				pass
