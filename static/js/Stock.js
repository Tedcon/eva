/*
 * Created on 2013-06-17.
 * @author: chengtingitng
 * @desc: 股票代码自动不全
 * @参数说明：
 * service: 获取数据接口
 * type: 接口最后拼接片段(stock：/stock:1，fund：/fund:1)
 * maxResultNum: 最多显示几行，默认10
 * fill: 点击或是enter时，input用什么填充：code(股票代码)，name(股票名称)，默认整个填充
 * @其他说明
 * service + val + type (完整接口)
 * 
 */
Stock = function(){
	this.filled = false;		// input是否填充
	this.listIndex = -1;		// 当前高亮元素下标
	this.url = '/spell/searchSuggest';
};

Stock.prototype.stock = function(dom,opt){
	var self = this;
	self.data = [];
	self.$dom = dom;
	self.$input = $('input',self.$dom);
	self.$wrap = $('.blk_stock_resultWrap',self.$dom);
	self.opt = opt;
	self.opt.maxResultNum = self.opt.maxResultNum ? parseInt(self.opt.maxResultNum) : 10;
	self.opt.type = self.opt.type ? self.opt.type : '';
	self.opt.service = self.opt.service ? self.opt.service : self.url;
	self.keydown();
	self.keyup();
	self.focus();
};

Stock.prototype.keydown = function(){
	var self = this;
	self.$input.keydown(function(event){
		switch(event.keyCode){
			case 13: 			// enter
				if(!self.filled && self.$wrap.is(':visible')){
					self.fillInput(self.listIndex);
				}
				self.$wrap.html('').hide();
				break;
			case 38: 			// up
				if(self.data.length>0){
					if(self.listIndex === 0){
						self.listIndex = self.data.length-1;
					}else{
						self.listIndex -= 1;
					}
					self.$list.removeClass('hover').eq(self.listIndex).addClass('hover');
					self.fillInput(self.listIndex);
				}
				break;
			case 40: 			// down
				if(self.data.length>0){
					if(self.listIndex < self.data.length-1){
						self.listIndex += 1;
					}else{
						self.listIndex = 0;
					}
					self.$list.removeClass('hover').eq(self.listIndex).addClass('hover');
					self.fillInput(self.listIndex);
				}
				break;
			default:
		}
	});
}

Stock.prototype.keyup = function(){
	var self = this;
	self.$input.keyup(function(event){
		var val = (self.$input.val()).replace(new RegExp("[\\s\\t\\xa0\\u3000]","g"),"");
		switch(event.keyCode){
			case 13: 			// enter
				break;
			case 38: 			// up
				break;
			case 40: 			// down
				break;
			default:
				if(val.length > 0 && val !== self.$input.data('oldVal')){
					self.filled = false;
					self.$input.data('oldVal',val);
					self.getResult(val);
				}
		}
	});
};

Stock.prototype.fillInput = function(i){
	var self = this;
	self.filled = true;
	switch(self.opt.fill){
		case 'code':
			self.$input.val(self.data[i][0]);
			break;
		case 'name':
			self.$input.val(self.data[i][1]);
			break;
		default:
			self.$input.val(self.data[i]);
	}
};

Stock.prototype.click = function(){
	var self = this;
	self.$list.click(function(){
		var index = $(this).index();
		self.fillInput(index);
		self.listIndex = -1;
	});
};

Stock.prototype.getResult = function(val){
	var self = this;
	$.ajax({
		url: self.opt.service + encodeURIComponent(val) + self.opt.type,
		type: 'get',
		success: function(data){
			var str = '';
			// data = '002030 达安基因 dajy,000423 东阿阿胶 daaj,002011 盾安环境 dahj,600288 大恒科技 dhkj,002236 大华股份 dhgf,002512 达华智能 dhzn,600257 大湖股份 dhgf,300103 达刚路机 dglj,002487 大金重工 djcg,000613 大东海A ddha',
			self.data = [];
			if(data && data.length > 0){
				if(typeof data === 'string'){
					data = data.split(',');
				}
				self.data = data;
				for(var i=0, len=data.length; i<len && i < self.opt.maxResultNum ; i++){
					str += '<li class="item">'+ data[i].replace(val,'<span class="keyword">'+ val +'</span>') +'</li>';
				}
				if(str.length>0){
					self.$wrap.html(str).show();
					self.$list = self.$wrap.find('li');
					self.listIndex = 0;
					self.$list.eq(0).addClass('hover');
					self.click();
					self.hover();
				}else{
					self.$wrap.hide();
				}
			}else{
				self.$wrap.html('').hide();
			}
		}
	});
};

Stock.prototype.hover = function(){
	var self = this;
	self.$list.hover(function(){
		var $this = $(this);
		self.$list.removeClass('hover');
		$this.addClass('hover');
		self.listIndex = $this.index();
	});
}

Stock.prototype.focus = function(){
	var self = this;
	self.$input.focus(function(){
		var val = (self.$input.val()).replace(new RegExp("[\\s\\t\\xa0\\u3000]","g"),"");
		if(val.length > 0 && val !== self.$input.attr('prompt')){
			self.getResult(val);
		}
	}).blur(function(){
		setTimeout(function(){
			self.$wrap.hide();
		},300);
	});
};

$.fn.autoComple = function(opt){
	this.each(function(){
		new Stock().stock($(this),opt);
	});
};
