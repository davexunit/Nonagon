<<<<<<< HEAD

    

  

<!DOCTYPE html>
<html>
  <head>
    <meta charset='utf-8'>
    <meta http-equiv="X-UA-Compatible" content="chrome=1">
        <title>model/game.py at 5feb85dd3592cc98309241c48e83a9d4bc5f60a3 from davexunit/PyweekWSU - GitHub</title>
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub" />
    <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub" />

    <link href="https://d3nwyuy0nl342s.cloudfront.net/a67846c79191434db05ae73c70e40a3a96870867/stylesheets/bundle_common.css" media="screen" rel="stylesheet" type="text/css" />
<link href="https://d3nwyuy0nl342s.cloudfront.net/a67846c79191434db05ae73c70e40a3a96870867/stylesheets/bundle_github.css" media="screen" rel="stylesheet" type="text/css" />
    

    <script type="text/javascript">
      if (typeof console == "undefined" || typeof console.log == "undefined")
        console = { log: function() {} }
    </script>
    <script type="text/javascript" charset="utf-8">
      var GitHub = {
        assetHost: 'https://d3nwyuy0nl342s.cloudfront.net'
      }
      var github_user = 'skarrmann'
      
    </script>
    <script src="https://d3nwyuy0nl342s.cloudfront.net/a67846c79191434db05ae73c70e40a3a96870867/javascripts/jquery/jquery-1.4.2.min.js" type="text/javascript"></script>
    <script src="https://d3nwyuy0nl342s.cloudfront.net/a67846c79191434db05ae73c70e40a3a96870867/javascripts/bundle_common.js" type="text/javascript"></script>
<script src="https://d3nwyuy0nl342s.cloudfront.net/a67846c79191434db05ae73c70e40a3a96870867/javascripts/bundle_github.js" type="text/javascript"></script>


    
    <script type="text/javascript" charset="utf-8">
      GitHub.spy({
        repo: "davexunit/PyweekWSU"
      })
    </script>

    
  <link href="https://github.com/davexunit/PyweekWSU/commits/5feb85dd3592cc98309241c48e83a9d4bc5f60a3.atom" rel="alternate" title="Recent Commits to PyweekWSU:5feb85dd3592cc98309241c48e83a9d4bc5f60a3" type="application/atom+xml" />

    <META NAME="ROBOTS" CONTENT="NOINDEX, FOLLOW">    <meta name="description" content="Entry for Pyweek game dev competition April 2011 PARTY HARD" />
    <script type="text/javascript">
      GitHub.nameWithOwner = GitHub.nameWithOwner || "davexunit/PyweekWSU";
      GitHub.currentRef = '';
      GitHub.commitSHA = "5feb85dd3592cc98309241c48e83a9d4bc5f60a3";
      GitHub.currentPath = 'model/game.py';
      GitHub.masterBranch = "master";

      
    </script>
  

        <script type="text/javascript">
      var _gaq = _gaq || [];
      _gaq.push(['_setAccount', 'UA-3769691-2']);
      _gaq.push(['_setDomainName', 'none']);
      _gaq.push(['_trackPageview']);
      (function() {
        var ga = document.createElement('script');
        ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
        ga.setAttribute('async', 'true');
        document.documentElement.firstChild.appendChild(ga);
      })();
    </script>

    
  </head>

  

  <body class="logged_in page-blob">
    

    

    

    

    

    <div class="subnavd" id="main">
      <div id="header" class="true">
        
          <a class="logo boring" href="https://github.com/">
            <img alt="github" class="default" src="https://d3nwyuy0nl342s.cloudfront.net/images/modules/header/logov3.png" />
            <!--[if (gt IE 8)|!(IE)]><!-->
            <img alt="github" class="hover" src="https://d3nwyuy0nl342s.cloudfront.net/images/modules/header/logov3-hover.png" />
            <!--<![endif]-->
          </a>
        
        
          





  
    <div class="userbox">
      <div class="avatarname">
        <a href="https://github.com/skarrmann"><img src="https://secure.gravatar.com/avatar/dcd6b9202f048a4271867bc3a778f799?s=140&d=https://d3nwyuy0nl342s.cloudfront.net%2Fimages%2Fgravatars%2Fgravatar-140.png" alt="" width="20" height="20"  /></a>
        <a href="https://github.com/skarrmann" class="name">skarrmann</a>

        
        
      </div>
      <ul class="usernav">
        <li><a href="https://github.com/">Dashboard</a></li>
        <li>
          
          <a href="https://github.com/inbox">Inbox</a>
          <a href="https://github.com/inbox" class="unread_count ">0</a>
        </li>
        <li><a href="https://github.com/account">Account Settings</a></li>
                <li><a href="/logout">Log Out</a></li>
      </ul>
    </div><!-- /.userbox -->
  


        
        <div class="topsearch">
  
    <form action="/search" id="top_search_form" method="get">
      <a href="/search" class="advanced-search tooltipped downwards" title="Advanced Search">Advanced Search</a>
      <input type="search" class="search my_repos_autocompleter" name="q" results="5" placeholder="Search&hellip;" /> <input type="submit" value="Search" class="button" />
      <input type="hidden" name="type" value="Everything" />
      <input type="hidden" name="repo" value="" />
      <input type="hidden" name="langOverride" value="" />
      <input type="hidden" name="start_value" value="1" />
    </form>
    <ul class="nav">
      <li><a href="/explore">Explore GitHub</a></li>
      <li><a href="https://gist.github.com">Gist</a></li>
      <li><a href="/blog">Blog</a></li>
      <li><a href="http://help.github.com">Help</a></li>
    </ul>
  
</div>

      </div>

      
      
        
    <div class="site">
      <div class="pagehead repohead vis-public    instapaper_ignore readability-menu">

      

      <div class="title-actions-bar">
        <h1>
          <a href="/davexunit">davexunit</a> / <strong><a href="https://github.com/davexunit/PyweekWSU">PyweekWSU</a></strong>
          
          
        </h1>

        
    <ul class="actions">
      

      
        <li class="for-owner" style="display:none"><a href="https://github.com/davexunit/PyweekWSU/admin" class="minibutton btn-admin "><span><span class="icon"></span>Admin</span></a></li>
        <li>
          <a href="/davexunit/PyweekWSU/toggle_watch" class="minibutton btn-watch " id="watch_button" onclick="var f = document.createElement('form'); f.style.display = 'none'; this.parentNode.appendChild(f); f.method = 'POST'; f.action = this.href;var s = document.createElement('input'); s.setAttribute('type', 'hidden'); s.setAttribute('name', 'authenticity_token'); s.setAttribute('value', '89efacf64308c6a640927f40e257c40abe2da29f'); f.appendChild(s);f.submit();return false;" style="display:none"><span><span class="icon"></span>Watch</span></a>
          <a href="/davexunit/PyweekWSU/toggle_watch" class="minibutton btn-watch " id="unwatch_button" onclick="var f = document.createElement('form'); f.style.display = 'none'; this.parentNode.appendChild(f); f.method = 'POST'; f.action = this.href;var s = document.createElement('input'); s.setAttribute('type', 'hidden'); s.setAttribute('name', 'authenticity_token'); s.setAttribute('value', '89efacf64308c6a640927f40e257c40abe2da29f'); f.appendChild(s);f.submit();return false;" style="display:none"><span><span class="icon"></span>Unwatch</span></a>
        </li>
        
          
            <li class="for-notforked" style="display:none"><a href="/davexunit/PyweekWSU/fork" class="minibutton btn-fork " id="fork_button" onclick="var f = document.createElement('form'); f.style.display = 'none'; this.parentNode.appendChild(f); f.method = 'POST'; f.action = this.href;var s = document.createElement('input'); s.setAttribute('type', 'hidden'); s.setAttribute('name', 'authenticity_token'); s.setAttribute('value', '89efacf64308c6a640927f40e257c40abe2da29f'); f.appendChild(s);f.submit();return false;"><span><span class="icon"></span>Fork</span></a></li>
            <li class="for-hasfork" style="display:none"><a href="#" class="minibutton btn-fork " id="your_fork_button"><span><span class="icon"></span>Your Fork</span></a></li>
          

          <li id='pull_request_item' class='nspr' style='display:none'><a href="/davexunit/PyweekWSU/pull/new/5feb85dd3592cc98309241c48e83a9d4bc5f60a3" class="minibutton btn-pull-request "><span><span class="icon"></span>Pull Request</span></a></li>
        
      
      
      <li class="repostats">
        <ul class="repo-stats">
          <li class="watchers"><a href="/davexunit/PyweekWSU/watchers" title="Watchers" class="tooltipped downwards">3</a></li>
          <li class="forks"><a href="/davexunit/PyweekWSU/network" title="Forks" class="tooltipped downwards">3</a></li>
        </ul>
      </li>
    </ul>

      </div>

        
  <ul class="tabs">
    <li><a href="https://github.com/davexunit/PyweekWSU/tree/" class="selected" highlight="repo_source">Source</a></li>
    <li><a href="https://github.com/davexunit/PyweekWSU/commits/" highlight="repo_commits">Commits</a></li>
    <li><a href="/davexunit/PyweekWSU/network" highlight="repo_network">Network</a></li>
    <li><a href="/davexunit/PyweekWSU/pulls" highlight="repo_pulls">Pull Requests (0)</a></li>

    

    
      
      <li><a href="/davexunit/PyweekWSU/issues" highlight="issues">Issues (0)</a></li>
    

            
    <li><a href="/davexunit/PyweekWSU/graphs" highlight="repo_graphs">Graphs</a></li>

    <li class="contextswitch nochoices">
      <span class="toggle leftwards tooltipped" title="5feb85dd3592cc98309241c48e83a9d4bc5f60a3">
        <em>Tree:</em>
        <code>5feb85d</code>
      </span>
    </li>
  </ul>

  <div style="display:none" id="pl-description"><p><em class="placeholder">click here to add a description</em></p></div>
  <div style="display:none" id="pl-homepage"><p><em class="placeholder">click here to add a homepage</em></p></div>

  <div class="subnav-bar">
  
  <ul>
    <li>
      
      <a href="/davexunit/PyweekWSU/branches" class="dropdown">Switch Branches (1)</a>
      <ul>
        
          
          
            <li><a href="/davexunit/PyweekWSU/blob/master/model/game.py" action="show">master</a></li>
          
        
      </ul>
    </li>
    <li>
      <a href="#" class="dropdown defunct">Switch Tags (0)</a>
      
    </li>
    <li>
    
    <a href="/davexunit/PyweekWSU/branches/master" class="manage">Branch List</a>
    
    </li>
  </ul>
</div>

  
  
  
  
  
  



        
    <div id="repo_details" class="metabox clearfix">
      <div id="repo_details_loader" class="metabox-loader" style="display:none">Sending Request&hellip;</div>

        <a href="/davexunit/PyweekWSU/downloads" class="download-source" id="download_button" title="Download source, tagged packages and binaries."><span class="icon"></span>Downloads</a>

      <div id="repository_desc_wrapper">
      <div id="repository_description" rel="repository_description_edit">
        
          <p>Entry for Pyweek game dev competition April 2011 PARTY HARD
            <span id="read_more" style="display:none">&mdash; <a href="#readme">Read more</a></span>
          </p>
        
      </div>

      <div id="repository_description_edit" style="display:none;" class="inline-edit">
        <form action="/davexunit/PyweekWSU/admin/update" method="post"><div style="margin:0;padding:0"><input name="authenticity_token" type="hidden" value="89efacf64308c6a640927f40e257c40abe2da29f" /></div>
          <input type="hidden" name="field" value="repository_description">
          <input type="text" class="textfield" name="value" value="Entry for Pyweek game dev competition April 2011 PARTY HARD">
          <div class="form-actions">
            <button class="minibutton"><span>Save</span></button> &nbsp; <a href="#" class="cancel">Cancel</a>
          </div>
        </form>
      </div>

      
      <div class="repository-homepage" id="repository_homepage" rel="repository_homepage_edit">
        <p><a href="http://lmgtfy.com" rel="nofollow">lmgtfy.com</a></p>
      </div>

      <div id="repository_homepage_edit" style="display:none;" class="inline-edit">
        <form action="/davexunit/PyweekWSU/admin/update" method="post"><div style="margin:0;padding:0"><input name="authenticity_token" type="hidden" value="89efacf64308c6a640927f40e257c40abe2da29f" /></div>
          <input type="hidden" name="field" value="repository_homepage">
          <input type="text" class="textfield" name="value" value="lmgtfy.com">
          <div class="form-actions">
            <button class="minibutton"><span>Save</span></button> &nbsp; <a href="#" class="cancel">Cancel</a>
          </div>
        </form>
      </div>
      </div>
      <div class="rule "></div>
            <div id="url_box" class="url-box">
        <ul class="clone-urls">
          
            
            <li id="http_clone_url"><a href="https://github.com/davexunit/PyweekWSU.git" data-permissions="Read-Only">HTTP</a></li>
            <li id="public_clone_url"><a href="git://github.com/davexunit/PyweekWSU.git" data-permissions="Read-Only">Git Read-Only</a></li>
          
          
        </ul>
        <input type="text" spellcheck="false" id="url_field" class="url-field" />
              <span style="display:none" id="url_box_clippy"></span>
      <span id="clippy_tooltip_url_box_clippy" class="clippy-tooltip tooltipped" title="copy to clipboard">
      <object classid="clsid:d27cdb6e-ae6d-11cf-96b8-444553540000"
              width="14"
              height="14"
              class="clippy"
              id="clippy" >
      <param name="movie" value="https://d3nwyuy0nl342s.cloudfront.net/flash/clippy.swf?v5"/>
      <param name="allowScriptAccess" value="always" />
      <param name="quality" value="high" />
      <param name="scale" value="noscale" />
      <param NAME="FlashVars" value="id=url_box_clippy&amp;copied=&amp;copyto=">
      <param name="bgcolor" value="#FFFFFF">
      <param name="wmode" value="opaque">
      <embed src="https://d3nwyuy0nl342s.cloudfront.net/flash/clippy.swf?v5"
             width="14"
             height="14"
             name="clippy"
             quality="high"
             allowScriptAccess="always"
             type="application/x-shockwave-flash"
             pluginspage="http://www.macromedia.com/go/getflashplayer"
             FlashVars="id=url_box_clippy&amp;copied=&amp;copyto="
             bgcolor="#FFFFFF"
             wmode="opaque"
      />
      </object>
      </span>

        <p id="url_description">This URL has <strong>Read+Write</strong> access</p>
      </div>
    </div>

    <div class="frame frame-center tree-finder" style="display:none">
      <div class="breadcrumb">
        <b><a href="/davexunit/PyweekWSU">PyweekWSU</a></b> /
        <input class="tree-finder-input" type="text" name="query" autocomplete="off" spellcheck="false">
      </div>

      
        <div class="octotip">
          <p>
            <a href="/davexunit/PyweekWSU/dismiss-tree-finder-help" class="dismiss js-dismiss-tree-list-help" title="Hide this notice forever">Dismiss</a>
            <strong>Octotip:</strong> You've activated the <em>file finder</em> by pressing <span class="kbd">t</span>
            Start typing to filter the file list. Use <span class="kbd badmono">↑</span> and <span class="kbd badmono">↓</span> to navigate,
            <span class="kbd">enter</span> to view files.
          </p>
        </div>
      

      <table class="tree-browser" cellpadding="0" cellspacing="0">
        <tr class="js-header"><th>&nbsp;</th><th>name</th></tr>
        <tr class="js-no-results no-results" style="display: none">
          <th colspan="2">No matching files</th>
        </tr>
        <tbody class="js-results-list">
        </tbody>
      </table>
    </div>

    <div id="jump-to-line" style="display:none">
      <h2>Jump to Line</h2>
      <form>
        <input class="textfield" type="text">
        <div class="full-button">
          <button type="submit" class="classy">
            <span>Go</span>
          </button>
        </div>
      </form>
    </div>


        

      </div><!-- /.pagehead -->

      

  





<script type="text/javascript">
  GitHub.downloadRepo = '/davexunit/PyweekWSU/archives/5feb85dd3592cc98309241c48e83a9d4bc5f60a3'
  GitHub.revType = "SHA1"

  GitHub.controllerName = "blob"
  GitHub.actionName     = "show"
  GitHub.currentAction  = "blob#show"

  
    GitHub.hasWriteAccess = false
    GitHub.hasAdminAccess = false
    GitHub.watchingRepo = true
    GitHub.ignoredRepo = false
    GitHub.hasForkOfRepo = "skarrmann/PyweekWSU"
    GitHub.hasForked = true
  

  
</script>






<div class="flash-messages"></div>


  <div id="commit">
    <div class="group">
        
  <div class="envelope commit">
    <div class="human">
      
        <div class="message"><pre><a href="/davexunit/PyweekWSU/commit/5feb85dd3592cc98309241c48e83a9d4bc5f60a3">Level creation framework is up and running</a> </pre></div>
      

      <div class="actor">
        <div class="gravatar">
          
          <img src="https://secure.gravatar.com/avatar/08c2c014224416323cc9195c69338cf7?s=140&d=https://d3nwyuy0nl342s.cloudfront.net%2Fimages%2Fgravatars%2Fgravatar-140.png" alt="" width="30" height="30"  />
        </div>
        <div class="name"><a href="/davexunit">davexunit</a> <span>(author)</span></div>
        <div class="date">
          <abbr class="relatize" title="2011-04-08 15:54:25">Fri Apr 08 15:54:25 -0700 2011</abbr>
        </div>
      </div>

      

    </div>
    <div class="machine">
      <span>c</span>ommit&nbsp;&nbsp;<a href="/davexunit/PyweekWSU/commit/5feb85dd3592cc98309241c48e83a9d4bc5f60a3" hotkey="c">5feb85dd3592cc983092</a><br />
      <span>t</span>ree&nbsp;&nbsp;&nbsp;&nbsp;<a href="/davexunit/PyweekWSU/tree/5feb85dd3592cc98309241c48e83a9d4bc5f60a3" hotkey="t">b739230a8c3d552e6311</a><br />
      
        <span>p</span>arent&nbsp;
        
        <a href="/davexunit/PyweekWSU/tree/7733b2821204331c7284bcc22db601baddb3856b" hotkey="p">7733b2821204331c7284</a>
      

    </div>
  </div>

    </div>
  </div>



  <div id="slider">

  

    <div class="breadcrumb" data-path="model/game.py/">
      <b><a href="/davexunit/PyweekWSU/tree/5feb85dd3592cc98309241c48e83a9d4bc5f60a3">PyweekWSU</a></b> / <a href="/davexunit/PyweekWSU/tree/5feb85dd3592cc98309241c48e83a9d4bc5f60a3/model">model</a> / game.py       <span style="display:none" id="clippy_1914">model/game.py</span>
      
      <object classid="clsid:d27cdb6e-ae6d-11cf-96b8-444553540000"
              width="110"
              height="14"
              class="clippy"
              id="clippy" >
      <param name="movie" value="https://d3nwyuy0nl342s.cloudfront.net/flash/clippy.swf?v5"/>
      <param name="allowScriptAccess" value="always" />
      <param name="quality" value="high" />
      <param name="scale" value="noscale" />
      <param NAME="FlashVars" value="id=clippy_1914&amp;copied=copied!&amp;copyto=copy to clipboard">
      <param name="bgcolor" value="#FFFFFF">
      <param name="wmode" value="opaque">
      <embed src="https://d3nwyuy0nl342s.cloudfront.net/flash/clippy.swf?v5"
             width="110"
             height="14"
             name="clippy"
             quality="high"
             allowScriptAccess="always"
             type="application/x-shockwave-flash"
             pluginspage="http://www.macromedia.com/go/getflashplayer"
             FlashVars="id=clippy_1914&amp;copied=copied!&amp;copyto=copy to clipboard"
             bgcolor="#FFFFFF"
             wmode="opaque"
      />
      </object>
      

    </div>

    <div class="frames">
      <div class="frame frame-center" data-path="model/game.py/">
        
          <ul class="big-actions">
            
            <li><a class="file-edit-link minibutton" href="/davexunit/PyweekWSU/file-edit/__current_ref__/model/game.py"><span>Edit this file</span></a></li>
          </ul>
        

        <div id="files">
          <div class="file">
            <div class="meta">
              <div class="info">
                <span class="icon"><img alt="Txt" height="16" src="https://d3nwyuy0nl342s.cloudfront.net/images/icons/txt.png" width="16" /></span>
                <span class="mode" title="File Mode">100644</span>
                
                  <span>501 lines (434 sloc)</span>
                
                <span>15.174 kb</span>
              </div>
              <ul class="actions">
                <li><a href="/davexunit/PyweekWSU/raw/5feb85dd3592cc98309241c48e83a9d4bc5f60a3/model/game.py" id="raw-url">raw</a></li>
                
                  <li><a href="/davexunit/PyweekWSU/blame/5feb85dd3592cc98309241c48e83a9d4bc5f60a3/model/game.py">blame</a></li>
                
                <li><a href="/davexunit/PyweekWSU/commits/5feb85dd3592cc98309241c48e83a9d4bc5f60a3/model/game.py">history</a></li>
              </ul>
            </div>
            
  <div class="data type-python">
    
      <table cellpadding="0" cellspacing="0">
        <tr>
          <td>
            <pre class="line_numbers"><span id="L1" rel="#L1">1</span>
<span id="L2" rel="#L2">2</span>
<span id="L3" rel="#L3">3</span>
<span id="L4" rel="#L4">4</span>
<span id="L5" rel="#L5">5</span>
<span id="L6" rel="#L6">6</span>
<span id="L7" rel="#L7">7</span>
<span id="L8" rel="#L8">8</span>
<span id="L9" rel="#L9">9</span>
<span id="L10" rel="#L10">10</span>
<span id="L11" rel="#L11">11</span>
<span id="L12" rel="#L12">12</span>
<span id="L13" rel="#L13">13</span>
<span id="L14" rel="#L14">14</span>
<span id="L15" rel="#L15">15</span>
<span id="L16" rel="#L16">16</span>
<span id="L17" rel="#L17">17</span>
<span id="L18" rel="#L18">18</span>
<span id="L19" rel="#L19">19</span>
<span id="L20" rel="#L20">20</span>
<span id="L21" rel="#L21">21</span>
<span id="L22" rel="#L22">22</span>
<span id="L23" rel="#L23">23</span>
<span id="L24" rel="#L24">24</span>
<span id="L25" rel="#L25">25</span>
<span id="L26" rel="#L26">26</span>
<span id="L27" rel="#L27">27</span>
<span id="L28" rel="#L28">28</span>
<span id="L29" rel="#L29">29</span>
<span id="L30" rel="#L30">30</span>
<span id="L31" rel="#L31">31</span>
<span id="L32" rel="#L32">32</span>
<span id="L33" rel="#L33">33</span>
<span id="L34" rel="#L34">34</span>
<span id="L35" rel="#L35">35</span>
<span id="L36" rel="#L36">36</span>
<span id="L37" rel="#L37">37</span>
<span id="L38" rel="#L38">38</span>
<span id="L39" rel="#L39">39</span>
<span id="L40" rel="#L40">40</span>
<span id="L41" rel="#L41">41</span>
<span id="L42" rel="#L42">42</span>
<span id="L43" rel="#L43">43</span>
<span id="L44" rel="#L44">44</span>
<span id="L45" rel="#L45">45</span>
<span id="L46" rel="#L46">46</span>
<span id="L47" rel="#L47">47</span>
<span id="L48" rel="#L48">48</span>
<span id="L49" rel="#L49">49</span>
<span id="L50" rel="#L50">50</span>
<span id="L51" rel="#L51">51</span>
<span id="L52" rel="#L52">52</span>
<span id="L53" rel="#L53">53</span>
<span id="L54" rel="#L54">54</span>
<span id="L55" rel="#L55">55</span>
<span id="L56" rel="#L56">56</span>
<span id="L57" rel="#L57">57</span>
<span id="L58" rel="#L58">58</span>
<span id="L59" rel="#L59">59</span>
<span id="L60" rel="#L60">60</span>
<span id="L61" rel="#L61">61</span>
<span id="L62" rel="#L62">62</span>
<span id="L63" rel="#L63">63</span>
<span id="L64" rel="#L64">64</span>
<span id="L65" rel="#L65">65</span>
<span id="L66" rel="#L66">66</span>
<span id="L67" rel="#L67">67</span>
<span id="L68" rel="#L68">68</span>
<span id="L69" rel="#L69">69</span>
<span id="L70" rel="#L70">70</span>
<span id="L71" rel="#L71">71</span>
<span id="L72" rel="#L72">72</span>
<span id="L73" rel="#L73">73</span>
<span id="L74" rel="#L74">74</span>
<span id="L75" rel="#L75">75</span>
<span id="L76" rel="#L76">76</span>
<span id="L77" rel="#L77">77</span>
<span id="L78" rel="#L78">78</span>
<span id="L79" rel="#L79">79</span>
<span id="L80" rel="#L80">80</span>
<span id="L81" rel="#L81">81</span>
<span id="L82" rel="#L82">82</span>
<span id="L83" rel="#L83">83</span>
<span id="L84" rel="#L84">84</span>
<span id="L85" rel="#L85">85</span>
<span id="L86" rel="#L86">86</span>
<span id="L87" rel="#L87">87</span>
<span id="L88" rel="#L88">88</span>
<span id="L89" rel="#L89">89</span>
<span id="L90" rel="#L90">90</span>
<span id="L91" rel="#L91">91</span>
<span id="L92" rel="#L92">92</span>
<span id="L93" rel="#L93">93</span>
<span id="L94" rel="#L94">94</span>
<span id="L95" rel="#L95">95</span>
<span id="L96" rel="#L96">96</span>
<span id="L97" rel="#L97">97</span>
<span id="L98" rel="#L98">98</span>
<span id="L99" rel="#L99">99</span>
<span id="L100" rel="#L100">100</span>
<span id="L101" rel="#L101">101</span>
<span id="L102" rel="#L102">102</span>
<span id="L103" rel="#L103">103</span>
<span id="L104" rel="#L104">104</span>
<span id="L105" rel="#L105">105</span>
<span id="L106" rel="#L106">106</span>
<span id="L107" rel="#L107">107</span>
<span id="L108" rel="#L108">108</span>
<span id="L109" rel="#L109">109</span>
<span id="L110" rel="#L110">110</span>
<span id="L111" rel="#L111">111</span>
<span id="L112" rel="#L112">112</span>
<span id="L113" rel="#L113">113</span>
<span id="L114" rel="#L114">114</span>
<span id="L115" rel="#L115">115</span>
<span id="L116" rel="#L116">116</span>
<span id="L117" rel="#L117">117</span>
<span id="L118" rel="#L118">118</span>
<span id="L119" rel="#L119">119</span>
<span id="L120" rel="#L120">120</span>
<span id="L121" rel="#L121">121</span>
<span id="L122" rel="#L122">122</span>
<span id="L123" rel="#L123">123</span>
<span id="L124" rel="#L124">124</span>
<span id="L125" rel="#L125">125</span>
<span id="L126" rel="#L126">126</span>
<span id="L127" rel="#L127">127</span>
<span id="L128" rel="#L128">128</span>
<span id="L129" rel="#L129">129</span>
<span id="L130" rel="#L130">130</span>
<span id="L131" rel="#L131">131</span>
<span id="L132" rel="#L132">132</span>
<span id="L133" rel="#L133">133</span>
<span id="L134" rel="#L134">134</span>
<span id="L135" rel="#L135">135</span>
<span id="L136" rel="#L136">136</span>
<span id="L137" rel="#L137">137</span>
<span id="L138" rel="#L138">138</span>
<span id="L139" rel="#L139">139</span>
<span id="L140" rel="#L140">140</span>
<span id="L141" rel="#L141">141</span>
<span id="L142" rel="#L142">142</span>
<span id="L143" rel="#L143">143</span>
<span id="L144" rel="#L144">144</span>
<span id="L145" rel="#L145">145</span>
<span id="L146" rel="#L146">146</span>
<span id="L147" rel="#L147">147</span>
<span id="L148" rel="#L148">148</span>
<span id="L149" rel="#L149">149</span>
<span id="L150" rel="#L150">150</span>
<span id="L151" rel="#L151">151</span>
<span id="L152" rel="#L152">152</span>
<span id="L153" rel="#L153">153</span>
<span id="L154" rel="#L154">154</span>
<span id="L155" rel="#L155">155</span>
<span id="L156" rel="#L156">156</span>
<span id="L157" rel="#L157">157</span>
<span id="L158" rel="#L158">158</span>
<span id="L159" rel="#L159">159</span>
<span id="L160" rel="#L160">160</span>
<span id="L161" rel="#L161">161</span>
<span id="L162" rel="#L162">162</span>
<span id="L163" rel="#L163">163</span>
<span id="L164" rel="#L164">164</span>
<span id="L165" rel="#L165">165</span>
<span id="L166" rel="#L166">166</span>
<span id="L167" rel="#L167">167</span>
<span id="L168" rel="#L168">168</span>
<span id="L169" rel="#L169">169</span>
<span id="L170" rel="#L170">170</span>
<span id="L171" rel="#L171">171</span>
<span id="L172" rel="#L172">172</span>
<span id="L173" rel="#L173">173</span>
<span id="L174" rel="#L174">174</span>
<span id="L175" rel="#L175">175</span>
<span id="L176" rel="#L176">176</span>
<span id="L177" rel="#L177">177</span>
<span id="L178" rel="#L178">178</span>
<span id="L179" rel="#L179">179</span>
<span id="L180" rel="#L180">180</span>
<span id="L181" rel="#L181">181</span>
<span id="L182" rel="#L182">182</span>
<span id="L183" rel="#L183">183</span>
<span id="L184" rel="#L184">184</span>
<span id="L185" rel="#L185">185</span>
<span id="L186" rel="#L186">186</span>
<span id="L187" rel="#L187">187</span>
<span id="L188" rel="#L188">188</span>
<span id="L189" rel="#L189">189</span>
<span id="L190" rel="#L190">190</span>
<span id="L191" rel="#L191">191</span>
<span id="L192" rel="#L192">192</span>
<span id="L193" rel="#L193">193</span>
<span id="L194" rel="#L194">194</span>
<span id="L195" rel="#L195">195</span>
<span id="L196" rel="#L196">196</span>
<span id="L197" rel="#L197">197</span>
<span id="L198" rel="#L198">198</span>
<span id="L199" rel="#L199">199</span>
<span id="L200" rel="#L200">200</span>
<span id="L201" rel="#L201">201</span>
<span id="L202" rel="#L202">202</span>
<span id="L203" rel="#L203">203</span>
<span id="L204" rel="#L204">204</span>
<span id="L205" rel="#L205">205</span>
<span id="L206" rel="#L206">206</span>
<span id="L207" rel="#L207">207</span>
<span id="L208" rel="#L208">208</span>
<span id="L209" rel="#L209">209</span>
<span id="L210" rel="#L210">210</span>
<span id="L211" rel="#L211">211</span>
<span id="L212" rel="#L212">212</span>
<span id="L213" rel="#L213">213</span>
<span id="L214" rel="#L214">214</span>
<span id="L215" rel="#L215">215</span>
<span id="L216" rel="#L216">216</span>
<span id="L217" rel="#L217">217</span>
<span id="L218" rel="#L218">218</span>
<span id="L219" rel="#L219">219</span>
<span id="L220" rel="#L220">220</span>
<span id="L221" rel="#L221">221</span>
<span id="L222" rel="#L222">222</span>
<span id="L223" rel="#L223">223</span>
<span id="L224" rel="#L224">224</span>
<span id="L225" rel="#L225">225</span>
<span id="L226" rel="#L226">226</span>
<span id="L227" rel="#L227">227</span>
<span id="L228" rel="#L228">228</span>
<span id="L229" rel="#L229">229</span>
<span id="L230" rel="#L230">230</span>
<span id="L231" rel="#L231">231</span>
<span id="L232" rel="#L232">232</span>
<span id="L233" rel="#L233">233</span>
<span id="L234" rel="#L234">234</span>
<span id="L235" rel="#L235">235</span>
<span id="L236" rel="#L236">236</span>
<span id="L237" rel="#L237">237</span>
<span id="L238" rel="#L238">238</span>
<span id="L239" rel="#L239">239</span>
<span id="L240" rel="#L240">240</span>
<span id="L241" rel="#L241">241</span>
<span id="L242" rel="#L242">242</span>
<span id="L243" rel="#L243">243</span>
<span id="L244" rel="#L244">244</span>
<span id="L245" rel="#L245">245</span>
<span id="L246" rel="#L246">246</span>
<span id="L247" rel="#L247">247</span>
<span id="L248" rel="#L248">248</span>
<span id="L249" rel="#L249">249</span>
<span id="L250" rel="#L250">250</span>
<span id="L251" rel="#L251">251</span>
<span id="L252" rel="#L252">252</span>
<span id="L253" rel="#L253">253</span>
<span id="L254" rel="#L254">254</span>
<span id="L255" rel="#L255">255</span>
<span id="L256" rel="#L256">256</span>
<span id="L257" rel="#L257">257</span>
<span id="L258" rel="#L258">258</span>
<span id="L259" rel="#L259">259</span>
<span id="L260" rel="#L260">260</span>
<span id="L261" rel="#L261">261</span>
<span id="L262" rel="#L262">262</span>
<span id="L263" rel="#L263">263</span>
<span id="L264" rel="#L264">264</span>
<span id="L265" rel="#L265">265</span>
<span id="L266" rel="#L266">266</span>
<span id="L267" rel="#L267">267</span>
<span id="L268" rel="#L268">268</span>
<span id="L269" rel="#L269">269</span>
<span id="L270" rel="#L270">270</span>
<span id="L271" rel="#L271">271</span>
<span id="L272" rel="#L272">272</span>
<span id="L273" rel="#L273">273</span>
<span id="L274" rel="#L274">274</span>
<span id="L275" rel="#L275">275</span>
<span id="L276" rel="#L276">276</span>
<span id="L277" rel="#L277">277</span>
<span id="L278" rel="#L278">278</span>
<span id="L279" rel="#L279">279</span>
<span id="L280" rel="#L280">280</span>
<span id="L281" rel="#L281">281</span>
<span id="L282" rel="#L282">282</span>
<span id="L283" rel="#L283">283</span>
<span id="L284" rel="#L284">284</span>
<span id="L285" rel="#L285">285</span>
<span id="L286" rel="#L286">286</span>
<span id="L287" rel="#L287">287</span>
<span id="L288" rel="#L288">288</span>
<span id="L289" rel="#L289">289</span>
<span id="L290" rel="#L290">290</span>
<span id="L291" rel="#L291">291</span>
<span id="L292" rel="#L292">292</span>
<span id="L293" rel="#L293">293</span>
<span id="L294" rel="#L294">294</span>
<span id="L295" rel="#L295">295</span>
<span id="L296" rel="#L296">296</span>
<span id="L297" rel="#L297">297</span>
<span id="L298" rel="#L298">298</span>
<span id="L299" rel="#L299">299</span>
<span id="L300" rel="#L300">300</span>
<span id="L301" rel="#L301">301</span>
<span id="L302" rel="#L302">302</span>
<span id="L303" rel="#L303">303</span>
<span id="L304" rel="#L304">304</span>
<span id="L305" rel="#L305">305</span>
<span id="L306" rel="#L306">306</span>
<span id="L307" rel="#L307">307</span>
<span id="L308" rel="#L308">308</span>
<span id="L309" rel="#L309">309</span>
<span id="L310" rel="#L310">310</span>
<span id="L311" rel="#L311">311</span>
<span id="L312" rel="#L312">312</span>
<span id="L313" rel="#L313">313</span>
<span id="L314" rel="#L314">314</span>
<span id="L315" rel="#L315">315</span>
<span id="L316" rel="#L316">316</span>
<span id="L317" rel="#L317">317</span>
<span id="L318" rel="#L318">318</span>
<span id="L319" rel="#L319">319</span>
<span id="L320" rel="#L320">320</span>
<span id="L321" rel="#L321">321</span>
<span id="L322" rel="#L322">322</span>
<span id="L323" rel="#L323">323</span>
<span id="L324" rel="#L324">324</span>
<span id="L325" rel="#L325">325</span>
<span id="L326" rel="#L326">326</span>
<span id="L327" rel="#L327">327</span>
<span id="L328" rel="#L328">328</span>
<span id="L329" rel="#L329">329</span>
<span id="L330" rel="#L330">330</span>
<span id="L331" rel="#L331">331</span>
<span id="L332" rel="#L332">332</span>
<span id="L333" rel="#L333">333</span>
<span id="L334" rel="#L334">334</span>
<span id="L335" rel="#L335">335</span>
<span id="L336" rel="#L336">336</span>
<span id="L337" rel="#L337">337</span>
<span id="L338" rel="#L338">338</span>
<span id="L339" rel="#L339">339</span>
<span id="L340" rel="#L340">340</span>
<span id="L341" rel="#L341">341</span>
<span id="L342" rel="#L342">342</span>
<span id="L343" rel="#L343">343</span>
<span id="L344" rel="#L344">344</span>
<span id="L345" rel="#L345">345</span>
<span id="L346" rel="#L346">346</span>
<span id="L347" rel="#L347">347</span>
<span id="L348" rel="#L348">348</span>
<span id="L349" rel="#L349">349</span>
<span id="L350" rel="#L350">350</span>
<span id="L351" rel="#L351">351</span>
<span id="L352" rel="#L352">352</span>
<span id="L353" rel="#L353">353</span>
<span id="L354" rel="#L354">354</span>
<span id="L355" rel="#L355">355</span>
<span id="L356" rel="#L356">356</span>
<span id="L357" rel="#L357">357</span>
<span id="L358" rel="#L358">358</span>
<span id="L359" rel="#L359">359</span>
<span id="L360" rel="#L360">360</span>
<span id="L361" rel="#L361">361</span>
<span id="L362" rel="#L362">362</span>
<span id="L363" rel="#L363">363</span>
<span id="L364" rel="#L364">364</span>
<span id="L365" rel="#L365">365</span>
<span id="L366" rel="#L366">366</span>
<span id="L367" rel="#L367">367</span>
<span id="L368" rel="#L368">368</span>
<span id="L369" rel="#L369">369</span>
<span id="L370" rel="#L370">370</span>
<span id="L371" rel="#L371">371</span>
<span id="L372" rel="#L372">372</span>
<span id="L373" rel="#L373">373</span>
<span id="L374" rel="#L374">374</span>
<span id="L375" rel="#L375">375</span>
<span id="L376" rel="#L376">376</span>
<span id="L377" rel="#L377">377</span>
<span id="L378" rel="#L378">378</span>
<span id="L379" rel="#L379">379</span>
<span id="L380" rel="#L380">380</span>
<span id="L381" rel="#L381">381</span>
<span id="L382" rel="#L382">382</span>
<span id="L383" rel="#L383">383</span>
<span id="L384" rel="#L384">384</span>
<span id="L385" rel="#L385">385</span>
<span id="L386" rel="#L386">386</span>
<span id="L387" rel="#L387">387</span>
<span id="L388" rel="#L388">388</span>
<span id="L389" rel="#L389">389</span>
<span id="L390" rel="#L390">390</span>
<span id="L391" rel="#L391">391</span>
<span id="L392" rel="#L392">392</span>
<span id="L393" rel="#L393">393</span>
<span id="L394" rel="#L394">394</span>
<span id="L395" rel="#L395">395</span>
<span id="L396" rel="#L396">396</span>
<span id="L397" rel="#L397">397</span>
<span id="L398" rel="#L398">398</span>
<span id="L399" rel="#L399">399</span>
<span id="L400" rel="#L400">400</span>
<span id="L401" rel="#L401">401</span>
<span id="L402" rel="#L402">402</span>
<span id="L403" rel="#L403">403</span>
<span id="L404" rel="#L404">404</span>
<span id="L405" rel="#L405">405</span>
<span id="L406" rel="#L406">406</span>
<span id="L407" rel="#L407">407</span>
<span id="L408" rel="#L408">408</span>
<span id="L409" rel="#L409">409</span>
<span id="L410" rel="#L410">410</span>
<span id="L411" rel="#L411">411</span>
<span id="L412" rel="#L412">412</span>
<span id="L413" rel="#L413">413</span>
<span id="L414" rel="#L414">414</span>
<span id="L415" rel="#L415">415</span>
<span id="L416" rel="#L416">416</span>
<span id="L417" rel="#L417">417</span>
<span id="L418" rel="#L418">418</span>
<span id="L419" rel="#L419">419</span>
<span id="L420" rel="#L420">420</span>
<span id="L421" rel="#L421">421</span>
<span id="L422" rel="#L422">422</span>
<span id="L423" rel="#L423">423</span>
<span id="L424" rel="#L424">424</span>
<span id="L425" rel="#L425">425</span>
<span id="L426" rel="#L426">426</span>
<span id="L427" rel="#L427">427</span>
<span id="L428" rel="#L428">428</span>
<span id="L429" rel="#L429">429</span>
<span id="L430" rel="#L430">430</span>
<span id="L431" rel="#L431">431</span>
<span id="L432" rel="#L432">432</span>
<span id="L433" rel="#L433">433</span>
<span id="L434" rel="#L434">434</span>
<span id="L435" rel="#L435">435</span>
<span id="L436" rel="#L436">436</span>
<span id="L437" rel="#L437">437</span>
<span id="L438" rel="#L438">438</span>
<span id="L439" rel="#L439">439</span>
<span id="L440" rel="#L440">440</span>
<span id="L441" rel="#L441">441</span>
<span id="L442" rel="#L442">442</span>
<span id="L443" rel="#L443">443</span>
<span id="L444" rel="#L444">444</span>
<span id="L445" rel="#L445">445</span>
<span id="L446" rel="#L446">446</span>
<span id="L447" rel="#L447">447</span>
<span id="L448" rel="#L448">448</span>
<span id="L449" rel="#L449">449</span>
<span id="L450" rel="#L450">450</span>
<span id="L451" rel="#L451">451</span>
<span id="L452" rel="#L452">452</span>
<span id="L453" rel="#L453">453</span>
<span id="L454" rel="#L454">454</span>
<span id="L455" rel="#L455">455</span>
<span id="L456" rel="#L456">456</span>
<span id="L457" rel="#L457">457</span>
<span id="L458" rel="#L458">458</span>
<span id="L459" rel="#L459">459</span>
<span id="L460" rel="#L460">460</span>
<span id="L461" rel="#L461">461</span>
<span id="L462" rel="#L462">462</span>
<span id="L463" rel="#L463">463</span>
<span id="L464" rel="#L464">464</span>
<span id="L465" rel="#L465">465</span>
<span id="L466" rel="#L466">466</span>
<span id="L467" rel="#L467">467</span>
<span id="L468" rel="#L468">468</span>
<span id="L469" rel="#L469">469</span>
<span id="L470" rel="#L470">470</span>
<span id="L471" rel="#L471">471</span>
<span id="L472" rel="#L472">472</span>
<span id="L473" rel="#L473">473</span>
<span id="L474" rel="#L474">474</span>
<span id="L475" rel="#L475">475</span>
<span id="L476" rel="#L476">476</span>
<span id="L477" rel="#L477">477</span>
<span id="L478" rel="#L478">478</span>
<span id="L479" rel="#L479">479</span>
<span id="L480" rel="#L480">480</span>
<span id="L481" rel="#L481">481</span>
<span id="L482" rel="#L482">482</span>
<span id="L483" rel="#L483">483</span>
<span id="L484" rel="#L484">484</span>
<span id="L485" rel="#L485">485</span>
<span id="L486" rel="#L486">486</span>
<span id="L487" rel="#L487">487</span>
<span id="L488" rel="#L488">488</span>
<span id="L489" rel="#L489">489</span>
<span id="L490" rel="#L490">490</span>
<span id="L491" rel="#L491">491</span>
<span id="L492" rel="#L492">492</span>
<span id="L493" rel="#L493">493</span>
<span id="L494" rel="#L494">494</span>
<span id="L495" rel="#L495">495</span>
<span id="L496" rel="#L496">496</span>
<span id="L497" rel="#L497">497</span>
<span id="L498" rel="#L498">498</span>
<span id="L499" rel="#L499">499</span>
<span id="L500" rel="#L500">500</span>
<span id="L501" rel="#L501">501</span>
</pre>
          </td>
          <td width="100%">
            
              
                <div class="highlight"><pre><div class='line' id='LC1'><span class="kn">import</span> <span class="nn">pyglet</span></div><div class='line' id='LC2'><span class="kn">from</span> <span class="nn">pyglet.gl</span> <span class="kn">import</span> <span class="o">*</span></div><div class='line' id='LC3'><span class="kn">import</span> <span class="nn">cocos</span></div><div class='line' id='LC4'><span class="kn">from</span> <span class="nn">cocos.director</span> <span class="kn">import</span> <span class="n">director</span></div><div class='line' id='LC5'><span class="kn">from</span> <span class="nn">cocos.actions</span> <span class="kn">import</span> <span class="o">*</span></div><div class='line' id='LC6'><span class="kn">from</span> <span class="nn">cocos.particle_systems</span> <span class="kn">import</span> <span class="n">Explosion</span></div><div class='line' id='LC7'><span class="kn">import</span> <span class="nn">math</span></div><div class='line' id='LC8'><span class="kn">import</span> <span class="nn">random</span></div><div class='line' id='LC9'><span class="kn">from</span> <span class="nn">collections</span> <span class="kn">import</span> <span class="n">deque</span></div><div class='line' id='LC10'><span class="kn">import</span> <span class="nn">level</span></div><div class='line' id='LC11'><br/></div><div class='line' id='LC12'><span class="k">class</span> <span class="nc">GameModel</span><span class="p">(</span><span class="n">pyglet</span><span class="o">.</span><span class="n">event</span><span class="o">.</span><span class="n">EventDispatcher</span><span class="p">):</span></div><div class='line' id='LC13'>	<span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC14'>		<span class="nb">super</span><span class="p">(</span><span class="n">GameModel</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="n">__init__</span><span class="p">()</span></div><div class='line' id='LC15'><br/></div><div class='line' id='LC16'>		<span class="bp">self</span><span class="o">.</span><span class="n">levels</span> <span class="o">=</span> <span class="n">deque</span><span class="p">()</span></div><div class='line' id='LC17'>		<span class="bp">self</span><span class="o">.</span><span class="n">current_level</span> <span class="o">=</span> <span class="bp">None</span></div><div class='line' id='LC18'>		<span class="c"># Testing wave class</span></div><div class='line' id='LC19'>		<span class="k">def</span> <span class="nf">make_action</span><span class="p">(</span><span class="n">enemy</span><span class="p">):</span></div><div class='line' id='LC20'>			<span class="n">path</span> <span class="o">=</span> <span class="n">level</span><span class="o">.</span><span class="n">create_enemy_path</span><span class="p">(</span><span class="n">enemy</span><span class="p">,</span> <span class="n">enemy</span><span class="o">.</span><span class="n">x</span> <span class="o">+</span> <span class="mi">100</span><span class="p">,</span> <span class="n">enemy</span><span class="o">.</span><span class="n">y</span> <span class="o">-</span> <span class="mi">150</span><span class="p">,</span> <span class="n">level</span><span class="o">.</span><span class="n">BEND_UP</span><span class="p">)</span></div><div class='line' id='LC21'>			<span class="k">return</span>  <span class="n">cocos</span><span class="o">.</span><span class="n">actions</span><span class="o">.</span><span class="n">Bezier</span><span class="p">(</span><span class="n">path</span><span class="p">,</span> <span class="mi">5</span><span class="p">)</span></div><div class='line' id='LC22'>		<span class="k">def</span> <span class="nf">make_weapon</span><span class="p">(</span><span class="n">enemy</span><span class="p">):</span></div><div class='line' id='LC23'>			<span class="k">return</span> <span class="n">BasicEnemyWeapon</span><span class="p">(</span><span class="n">enemy</span><span class="p">,</span> <span class="mi">1</span><span class="p">)</span></div><div class='line' id='LC24'>		<span class="n">enemy1</span> <span class="o">=</span> <span class="n">level</span><span class="o">.</span><span class="n">WaveEnemy</span><span class="p">(</span><span class="mi">3</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="n">make_action</span><span class="p">,</span> <span class="n">make_weapon</span><span class="p">)</span></div><div class='line' id='LC25'>		<span class="n">enemy2</span> <span class="o">=</span> <span class="n">level</span><span class="o">.</span><span class="n">WaveEnemy</span><span class="p">(</span><span class="mi">5</span><span class="p">,</span> <span class="mi">3</span><span class="p">,</span> <span class="n">make_action</span><span class="p">,</span> <span class="n">make_weapon</span><span class="p">)</span></div><div class='line' id='LC26'>		<span class="n">wave0</span> <span class="o">=</span> <span class="n">level</span><span class="o">.</span><span class="n">Wave</span><span class="p">(</span><span class="n">level</span><span class="o">.</span><span class="n">horizontalLayout</span><span class="p">(</span><span class="mi">600</span><span class="p">),</span> <span class="p">[</span><span class="n">enemy1</span><span class="p">,</span> <span class="n">enemy1</span><span class="p">,</span> <span class="n">enemy1</span><span class="p">,</span> <span class="n">enemy1</span><span class="p">])</span></div><div class='line' id='LC27'>		<span class="n">wave1</span> <span class="o">=</span> <span class="n">level</span><span class="o">.</span><span class="n">Wave</span><span class="p">(</span><span class="n">level</span><span class="o">.</span><span class="n">horizontalLayout</span><span class="p">(</span><span class="mi">500</span><span class="p">),</span> <span class="p">[</span><span class="n">enemy1</span><span class="p">,</span> <span class="n">enemy2</span><span class="p">,</span> <span class="n">enemy1</span><span class="p">,</span> <span class="n">enemy2</span><span class="p">])</span></div><div class='line' id='LC28'>		<span class="n">wave2</span> <span class="o">=</span> <span class="n">level</span><span class="o">.</span><span class="n">Wave</span><span class="p">(</span><span class="n">level</span><span class="o">.</span><span class="n">horizontalLayout</span><span class="p">(</span><span class="mi">400</span><span class="p">),</span> <span class="p">[</span><span class="n">enemy2</span><span class="p">,</span> <span class="n">enemy2</span><span class="p">,</span> <span class="n">enemy2</span><span class="p">,</span> <span class="n">enemy2</span><span class="p">])</span></div><div class='line' id='LC29'>		<span class="n">level1</span> <span class="o">=</span> <span class="n">level</span><span class="o">.</span><span class="n">Level</span><span class="p">([</span><span class="n">wave0</span><span class="p">,</span> <span class="n">wave1</span><span class="p">,</span> <span class="n">wave2</span><span class="p">])</span></div><div class='line' id='LC30'>		<span class="c">#wave3 = level.Wave([(6, None), (6, None), (6, None)])</span></div><div class='line' id='LC31'>		<span class="c">#wave4 = level.Wave([(7, None), (8, None)])</span></div><div class='line' id='LC32'>		<span class="c">#level2 = level.Level([wave3, wave4])</span></div><div class='line' id='LC33'>		<span class="bp">self</span><span class="o">.</span><span class="n">levels</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">level1</span><span class="p">)</span></div><div class='line' id='LC34'>		<span class="c">#self.levels.append(level2)</span></div><div class='line' id='LC35'><br/></div><div class='line' id='LC36'>		<span class="c"># Add the player</span></div><div class='line' id='LC37'>		<span class="bp">self</span><span class="o">.</span><span class="n">player</span> <span class="o">=</span> <span class="n">Player</span><span class="p">()</span></div><div class='line' id='LC38'>		<span class="bp">self</span><span class="o">.</span><span class="n">player</span><span class="o">.</span><span class="n">position</span> <span class="o">=</span> <span class="mi">400</span><span class="p">,</span> <span class="mi">300</span></div><div class='line' id='LC39'>		<span class="c"># Node for player bullets</span></div><div class='line' id='LC40'>		<span class="bp">self</span><span class="o">.</span><span class="n">player_bullets</span> <span class="o">=</span> <span class="n">cocos</span><span class="o">.</span><span class="n">batch</span><span class="o">.</span><span class="n">BatchNode</span><span class="p">()</span></div><div class='line' id='LC41'>		<span class="c"># Node for enemy bullets</span></div><div class='line' id='LC42'>		<span class="bp">self</span><span class="o">.</span><span class="n">enemy_bullets</span> <span class="o">=</span> <span class="n">cocos</span><span class="o">.</span><span class="n">batch</span><span class="o">.</span><span class="n">BatchNode</span><span class="p">()</span></div><div class='line' id='LC43'>		<span class="c"># Node for particles</span></div><div class='line' id='LC44'>		<span class="bp">self</span><span class="o">.</span><span class="n">particles</span> <span class="o">=</span> <span class="n">cocos</span><span class="o">.</span><span class="n">cocosnode</span><span class="o">.</span><span class="n">CocosNode</span><span class="p">()</span></div><div class='line' id='LC45'><br/></div><div class='line' id='LC46'>		<span class="c"># Register player event listeners</span></div><div class='line' id='LC47'>		<span class="bp">self</span><span class="o">.</span><span class="n">player</span><span class="o">.</span><span class="n">push_handlers</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span></div><div class='line' id='LC48'><br/></div><div class='line' id='LC49'>	<span class="k">def</span> <span class="nf">next_level</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC50'>		<span class="c"># No levels left? WE HAVE A WINRAR!</span></div><div class='line' id='LC51'>		<span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">levels</span><span class="p">)</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span></div><div class='line' id='LC52'>			<span class="kn">import</span> <span class="nn">getvictory</span></div><div class='line' id='LC53'>			<span class="n">director</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="n">getvictory</span><span class="o">.</span><span class="n">get_scene</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">player</span><span class="o">.</span><span class="n">score</span><span class="p">))</span></div><div class='line' id='LC54'>			<span class="k">return</span></div><div class='line' id='LC55'><br/></div><div class='line' id='LC56'>		<span class="bp">self</span><span class="o">.</span><span class="n">current_level</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">levels</span><span class="o">.</span><span class="n">popleft</span><span class="p">()</span></div><div class='line' id='LC57'>		<span class="bp">self</span><span class="o">.</span><span class="n">dispatch_event</span><span class="p">(</span><span class="s">&#39;on_new_level&#39;</span><span class="p">)</span></div><div class='line' id='LC58'>		<span class="bp">self</span><span class="o">.</span><span class="n">current_level</span><span class="o">.</span><span class="n">push_handlers</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span></div><div class='line' id='LC59'>		<span class="bp">self</span><span class="o">.</span><span class="n">current_level</span><span class="o">.</span><span class="n">next_wave</span><span class="p">()</span></div><div class='line' id='LC60'><br/></div><div class='line' id='LC61'>	<span class="k">def</span> <span class="nf">on_new_wave</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">wave</span><span class="p">):</span></div><div class='line' id='LC62'>		<span class="k">for</span> <span class="n">e</span> <span class="ow">in</span> <span class="n">wave</span><span class="o">.</span><span class="n">get_children</span><span class="p">():</span></div><div class='line' id='LC63'>			<span class="n">e</span><span class="o">.</span><span class="n">push_handlers</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span></div><div class='line' id='LC64'><br/></div><div class='line' id='LC65'>	<span class="k">def</span> <span class="nf">on_level_complete</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC66'>		<span class="bp">self</span><span class="o">.</span><span class="n">next_level</span><span class="p">()</span></div><div class='line' id='LC67'><br/></div><div class='line' id='LC68'>	<span class="k">def</span> <span class="nf">on_lose_life</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">lives</span><span class="p">):</span></div><div class='line' id='LC69'>		<span class="c"># Make an explosion particle effect</span></div><div class='line' id='LC70'>		<span class="n">p</span> <span class="o">=</span> <span class="n">Explosion</span><span class="p">()</span></div><div class='line' id='LC71'>		<span class="n">p</span><span class="o">.</span><span class="n">position</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">player</span><span class="o">.</span><span class="n">position</span></div><div class='line' id='LC72'>		<span class="bp">self</span><span class="o">.</span><span class="n">particles</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">p</span><span class="p">)</span></div><div class='line' id='LC73'>		<span class="c"># Reset the player to the center of the screen</span></div><div class='line' id='LC74'>		<span class="n">w</span><span class="p">,</span> <span class="n">h</span> <span class="o">=</span> <span class="n">director</span><span class="o">.</span><span class="n">get_window_size</span><span class="p">()</span></div><div class='line' id='LC75'>		<span class="bp">self</span><span class="o">.</span><span class="n">player</span><span class="o">.</span><span class="n">position</span> <span class="o">=</span> <span class="n">w</span><span class="o">/</span><span class="mi">2</span><span class="p">,</span> <span class="n">h</span><span class="o">/</span><span class="mi">2</span></div><div class='line' id='LC76'>		<span class="c"># If the player is out of lives it&#39;s game over.</span></div><div class='line' id='LC77'>		<span class="k">if</span> <span class="n">lives</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span></div><div class='line' id='LC78'>			<span class="kn">import</span> <span class="nn">getgameover</span></div><div class='line' id='LC79'>			<span class="n">director</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="n">getgameover</span><span class="o">.</span><span class="n">get_scene</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">player</span><span class="o">.</span><span class="n">score</span><span class="p">))</span></div><div class='line' id='LC80'><br/></div><div class='line' id='LC81'>	<span class="k">def</span> <span class="nf">on_bad_transform</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">enemy</span><span class="p">):</span></div><div class='line' id='LC82'>		<span class="bp">self</span><span class="o">.</span><span class="n">player</span><span class="o">.</span><span class="n">chain</span> <span class="o">=</span> <span class="mi">0</span></div><div class='line' id='LC83'><br/></div><div class='line' id='LC84'>	<span class="k">def</span> <span class="nf">on_enemy_death</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">enemy</span><span class="p">):</span></div><div class='line' id='LC85'>		<span class="bp">self</span><span class="o">.</span><span class="n">player</span><span class="o">.</span><span class="n">chain</span> <span class="o">+=</span> <span class="mi">1</span></div><div class='line' id='LC86'>		<span class="n">max_transforms</span> <span class="o">=</span> <span class="n">enemy</span><span class="o">.</span><span class="n">num_vertices</span> <span class="o">/</span> <span class="mi">2</span></div><div class='line' id='LC87'>		<span class="c"># Points multiplier</span></div><div class='line' id='LC88'>		<span class="c"># Full points awarded for taking n/2 or less transformations to kill enemy</span></div><div class='line' id='LC89'>		<span class="c"># Points reduced with each additional hit</span></div><div class='line' id='LC90'>		<span class="n">multiplier</span> <span class="o">=</span> <span class="n">max_transforms</span> <span class="o">/</span> <span class="nb">float</span><span class="p">(</span><span class="nb">max</span><span class="p">(</span><span class="n">max_transforms</span><span class="p">,</span> <span class="n">enemy</span><span class="o">.</span><span class="n">num_transforms</span><span class="p">))</span></div><div class='line' id='LC91'>		<span class="bp">self</span><span class="o">.</span><span class="n">player</span><span class="o">.</span><span class="n">score</span> <span class="o">+=</span> <span class="n">enemy</span><span class="o">.</span><span class="n">num_vertices</span> <span class="o">*</span> <span class="mi">10</span> <span class="o">*</span> <span class="n">multiplier</span></div><div class='line' id='LC92'>		<span class="n">p</span> <span class="o">=</span> <span class="n">Explosion</span><span class="p">()</span></div><div class='line' id='LC93'>		<span class="n">p</span><span class="o">.</span><span class="n">position</span> <span class="o">=</span> <span class="n">enemy</span><span class="o">.</span><span class="n">position</span></div><div class='line' id='LC94'>		<span class="bp">self</span><span class="o">.</span><span class="n">particles</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">p</span><span class="p">)</span></div><div class='line' id='LC95'><br/></div><div class='line' id='LC96'>	<span class="k">def</span> <span class="nf">on_player_fire</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">bullet</span><span class="p">):</span></div><div class='line' id='LC97'>		<span class="bp">self</span><span class="o">.</span><span class="n">player_bullets</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">bullet</span><span class="p">)</span></div><div class='line' id='LC98'><br/></div><div class='line' id='LC99'>	<span class="k">def</span> <span class="nf">on_enemy_fire</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">bullet</span><span class="p">):</span></div><div class='line' id='LC100'>		<span class="bp">self</span><span class="o">.</span><span class="n">enemy_bullets</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">bullet</span><span class="p">)</span></div><div class='line' id='LC101'><br/></div><div class='line' id='LC102'>	<span class="k">def</span> <span class="nf">step</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">dt</span><span class="p">):</span></div><div class='line' id='LC103'>		<span class="sd">&quot;&quot;&quot;Called every frame, this method updates objects that have time dependent calculations to perform.</span></div><div class='line' id='LC104'><span class="sd">		&quot;&quot;&quot;</span></div><div class='line' id='LC105'>		<span class="c"># Some inefficient naive collision detection</span></div><div class='line' id='LC106'>		<span class="k">for</span> <span class="n">b</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">player_bullets</span><span class="o">.</span><span class="n">get_children</span><span class="p">():</span></div><div class='line' id='LC107'>			<span class="k">for</span> <span class="n">e</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">current_level</span><span class="o">.</span><span class="n">current_wave</span><span class="o">.</span><span class="n">get_children</span><span class="p">():</span></div><div class='line' id='LC108'>				<span class="k">if</span> <span class="n">b</span><span class="o">.</span><span class="n">get_rect</span><span class="p">()</span><span class="o">.</span><span class="n">intersects</span><span class="p">(</span><span class="n">e</span><span class="o">.</span><span class="n">get_rect</span><span class="p">()):</span></div><div class='line' id='LC109'>					<span class="n">b</span><span class="o">.</span><span class="n">on_hit</span><span class="p">(</span><span class="n">e</span><span class="p">)</span></div><div class='line' id='LC110'>					<span class="bp">self</span><span class="o">.</span><span class="n">player_bullets</span><span class="o">.</span><span class="n">remove</span><span class="p">(</span><span class="n">b</span><span class="p">)</span></div><div class='line' id='LC111'>					<span class="k">return</span></div><div class='line' id='LC112'>		<span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">player</span><span class="o">.</span><span class="n">no_clip</span><span class="p">:</span></div><div class='line' id='LC113'>			<span class="k">for</span> <span class="n">e</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">current_level</span><span class="o">.</span><span class="n">current_wave</span><span class="o">.</span><span class="n">get_children</span><span class="p">():</span></div><div class='line' id='LC114'>				<span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">player</span><span class="o">.</span><span class="n">get_rect</span><span class="p">()</span><span class="o">.</span><span class="n">intersects</span><span class="p">(</span><span class="n">e</span><span class="o">.</span><span class="n">get_rect</span><span class="p">()):</span></div><div class='line' id='LC115'>					<span class="bp">self</span><span class="o">.</span><span class="n">player</span><span class="o">.</span><span class="n">on_hit</span><span class="p">()</span></div><div class='line' id='LC116'>					<span class="k">return</span></div><div class='line' id='LC117'>			<span class="k">for</span> <span class="n">b</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">enemy_bullets</span><span class="o">.</span><span class="n">get_children</span><span class="p">():</span></div><div class='line' id='LC118'>				<span class="k">if</span> <span class="n">b</span><span class="o">.</span><span class="n">get_rect</span><span class="p">()</span><span class="o">.</span><span class="n">intersects</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">player</span><span class="o">.</span><span class="n">get_rect</span><span class="p">()):</span></div><div class='line' id='LC119'>					<span class="n">b</span><span class="o">.</span><span class="n">on_hit</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">player</span><span class="p">)</span></div><div class='line' id='LC120'>					<span class="bp">self</span><span class="o">.</span><span class="n">enemy_bullets</span><span class="o">.</span><span class="n">remove</span><span class="p">(</span><span class="n">b</span><span class="p">)</span></div><div class='line' id='LC121'>					<span class="k">return</span></div><div class='line' id='LC122'><br/></div><div class='line' id='LC123'><span class="n">GameModel</span><span class="o">.</span><span class="n">register_event_type</span><span class="p">(</span><span class="s">&#39;on_new_level&#39;</span><span class="p">)</span></div><div class='line' id='LC124'><br/></div><div class='line' id='LC125'><span class="k">class</span> <span class="nc">RemoveBoundedMove</span><span class="p">(</span><span class="n">cocos</span><span class="o">.</span><span class="n">actions</span><span class="o">.</span><span class="n">move_actions</span><span class="o">.</span><span class="n">Move</span><span class="p">):</span></div><div class='line' id='LC126'>	<span class="sd">&quot;&quot;&quot;Move the target but remove it from the parent when it reaches certain bounds.</span></div><div class='line' id='LC127'><span class="sd">	Modified from the cocos2d sources to fit the needed purpose.</span></div><div class='line' id='LC128'><span class="sd">	This action is used for bullets.</span></div><div class='line' id='LC129'><span class="sd">	&quot;&quot;&quot;</span></div><div class='line' id='LC130'>	<span class="k">def</span> <span class="nf">init</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">width</span><span class="p">,</span> <span class="n">height</span><span class="p">):</span></div><div class='line' id='LC131'>		<span class="bp">self</span><span class="o">.</span><span class="n">width</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">height</span> <span class="o">=</span> <span class="n">width</span><span class="p">,</span> <span class="n">height</span></div><div class='line' id='LC132'><br/></div><div class='line' id='LC133'>	<span class="k">def</span> <span class="nf">step</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">dt</span><span class="p">):</span></div><div class='line' id='LC134'>		<span class="nb">super</span><span class="p">(</span><span class="n">RemoveBoundedMove</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="n">step</span><span class="p">(</span><span class="n">dt</span><span class="p">)</span></div><div class='line' id='LC135'>		<span class="n">x</span><span class="p">,</span> <span class="n">y</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">target</span><span class="o">.</span><span class="n">position</span></div><div class='line' id='LC136'>		<span class="n">w</span><span class="p">,</span> <span class="n">h</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">target</span><span class="o">.</span><span class="n">width</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">target</span><span class="o">.</span><span class="n">height</span></div><div class='line' id='LC137'>		<span class="c"># Out of bounds, remove the node from the parent</span></div><div class='line' id='LC138'>		<span class="k">if</span> <span class="n">x</span> <span class="o">&gt;</span> <span class="bp">self</span><span class="o">.</span><span class="n">width</span> <span class="o">+</span> <span class="n">w</span><span class="o">/</span><span class="mi">2</span> <span class="ow">or</span> <span class="n">x</span> <span class="o">&lt;</span> <span class="mi">0</span> <span class="o">-</span> <span class="n">w</span><span class="o">/</span><span class="mi">2</span> <span class="ow">or</span> <span class="n">y</span> <span class="o">&gt;</span> <span class="bp">self</span><span class="o">.</span><span class="n">height</span> <span class="o">+</span> <span class="n">h</span><span class="o">/</span><span class="mi">2</span> <span class="ow">or</span> <span class="n">y</span> <span class="o">&lt;</span> <span class="mi">0</span> <span class="o">-</span> <span class="n">h</span><span class="o">/</span><span class="mi">2</span><span class="p">:</span></div><div class='line' id='LC139'>			<span class="bp">self</span><span class="o">.</span><span class="n">target</span><span class="o">.</span><span class="n">parent</span><span class="o">.</span><span class="n">remove</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">target</span><span class="p">)</span></div><div class='line' id='LC140'><br/></div><div class='line' id='LC141'>		<span class="bp">self</span><span class="o">.</span><span class="n">target</span><span class="o">.</span><span class="n">position</span> <span class="o">=</span> <span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="n">y</span><span class="p">)</span></div><div class='line' id='LC142'><br/></div><div class='line' id='LC143'><span class="k">class</span> <span class="nc">Bullet</span><span class="p">(</span><span class="n">cocos</span><span class="o">.</span><span class="n">sprite</span><span class="o">.</span><span class="n">Sprite</span><span class="p">):</span></div><div class='line' id='LC144'>	<span class="sd">&quot;&quot;&quot;Provides the functionality to create differing bullet types by using event handlers.</span></div><div class='line' id='LC145'><span class="sd">	&quot;&quot;&quot;</span></div><div class='line' id='LC146'>	<span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">image_file</span><span class="p">,</span> <span class="n">dx</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span> <span class="n">dy</span><span class="o">=</span><span class="mi">500</span><span class="p">):</span></div><div class='line' id='LC147'>		<span class="sd">&quot;&quot;&quot;dx and dy parameters set the bullet speed and vector.</span></div><div class='line' id='LC148'><span class="sd">		&quot;&quot;&quot;</span></div><div class='line' id='LC149'>		<span class="nb">super</span><span class="p">(</span><span class="n">Bullet</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="n">__init__</span><span class="p">(</span><span class="n">image_file</span><span class="p">)</span></div><div class='line' id='LC150'>		<span class="bp">self</span><span class="o">.</span><span class="n">velocity</span> <span class="o">=</span> <span class="n">dx</span><span class="p">,</span> <span class="n">dy</span></div><div class='line' id='LC151'>		<span class="n">w</span><span class="p">,</span> <span class="n">h</span> <span class="o">=</span> <span class="n">director</span><span class="o">.</span><span class="n">get_window_size</span><span class="p">()</span></div><div class='line' id='LC152'>		<span class="bp">self</span><span class="o">.</span><span class="n">do</span><span class="p">(</span><span class="n">RemoveBoundedMove</span><span class="p">(</span><span class="n">w</span><span class="p">,</span> <span class="n">h</span><span class="p">))</span></div><div class='line' id='LC153'><br/></div><div class='line' id='LC154'>	<span class="k">def</span> <span class="nf">step</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">dt</span><span class="p">):</span></div><div class='line' id='LC155'>		<span class="bp">self</span><span class="o">.</span><span class="n">x</span> <span class="o">+=</span> <span class="bp">self</span><span class="o">.</span><span class="n">dx</span> <span class="o">*</span> <span class="n">dt</span></div><div class='line' id='LC156'>		<span class="bp">self</span><span class="o">.</span><span class="n">y</span> <span class="o">+=</span> <span class="bp">self</span><span class="o">.</span><span class="n">dy</span> <span class="o">*</span> <span class="n">dt</span></div><div class='line' id='LC157'><br/></div><div class='line' id='LC158'>	<span class="k">def</span> <span class="nf">on_hit</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">entity</span><span class="p">):</span></div><div class='line' id='LC159'>		<span class="sd">&quot;&quot;&quot;Hit event handler.</span></div><div class='line' id='LC160'><span class="sd">		Customize this to do what you want the bullet to do.</span></div><div class='line' id='LC161'><span class="sd">		&quot;&quot;&quot;</span></div><div class='line' id='LC162'>		<span class="k">pass</span></div><div class='line' id='LC163'><br/></div><div class='line' id='LC164'><span class="k">class</span> <span class="nc">RotateCWBullet</span><span class="p">(</span><span class="n">Bullet</span><span class="p">):</span></div><div class='line' id='LC165'>	<span class="sd">&quot;&quot;&quot;Bullet that will rotate an enemy&#39;s kill vertex one &#39;step&#39; clockwise.</span></div><div class='line' id='LC166'><span class="sd">	&quot;&quot;&quot;</span></div><div class='line' id='LC167'>	<span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC168'>		<span class="nb">super</span><span class="p">(</span><span class="n">RotateCWBullet</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="n">__init__</span><span class="p">(</span><span class="s">&#39;rotate_cw_bullet.png&#39;</span><span class="p">)</span></div><div class='line' id='LC169'><br/></div><div class='line' id='LC170'>	<span class="k">def</span> <span class="nf">on_hit</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">entity</span><span class="p">):</span></div><div class='line' id='LC171'>		<span class="k">if</span> <span class="n">entity</span><span class="o">.</span><span class="n">no_shield</span><span class="p">:</span></div><div class='line' id='LC172'>			<span class="n">entity</span><span class="o">.</span><span class="n">rotate_cw</span><span class="p">()</span></div><div class='line' id='LC173'><br/></div><div class='line' id='LC174'><span class="k">class</span> <span class="nc">RotateCCWBullet</span><span class="p">(</span><span class="n">Bullet</span><span class="p">):</span></div><div class='line' id='LC175'>	<span class="sd">&quot;&quot;&quot;Bullet that will rotate an enemy&#39;s kill vertex one &#39;step&#39; counter clockwise.</span></div><div class='line' id='LC176'><span class="sd">	&quot;&quot;&quot;</span></div><div class='line' id='LC177'>	<span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC178'>		<span class="nb">super</span><span class="p">(</span><span class="n">RotateCCWBullet</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="n">__init__</span><span class="p">(</span><span class="s">&#39;rotate_ccw_bullet.png&#39;</span><span class="p">)</span></div><div class='line' id='LC179'><br/></div><div class='line' id='LC180'>	<span class="k">def</span> <span class="nf">on_hit</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">entity</span><span class="p">):</span></div><div class='line' id='LC181'>		<span class="k">if</span> <span class="n">entity</span><span class="o">.</span><span class="n">no_shield</span><span class="p">:</span></div><div class='line' id='LC182'>			<span class="n">entity</span><span class="o">.</span><span class="n">rotate_ccw</span><span class="p">()</span></div><div class='line' id='LC183'><br/></div><div class='line' id='LC184'><span class="k">class</span> <span class="nc">FlipLeftBullet</span><span class="p">(</span><span class="n">Bullet</span><span class="p">):</span></div><div class='line' id='LC185'>	<span class="sd">&quot;&quot;&quot;Bullet that will flip an enemy by it&#39;s left axis of symmetry.</span></div><div class='line' id='LC186'><span class="sd">	&quot;&quot;&quot;</span></div><div class='line' id='LC187'>	<span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC188'>		<span class="nb">super</span><span class="p">(</span><span class="n">FlipLeftBullet</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="n">__init__</span><span class="p">(</span><span class="s">&#39;flip_left_bullet.png&#39;</span><span class="p">)</span></div><div class='line' id='LC189'><br/></div><div class='line' id='LC190'>	<span class="k">def</span> <span class="nf">on_hit</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">entity</span><span class="p">):</span></div><div class='line' id='LC191'>		<span class="k">if</span> <span class="n">entity</span><span class="o">.</span><span class="n">no_shield</span><span class="p">:</span></div><div class='line' id='LC192'>			<span class="n">entity</span><span class="o">.</span><span class="n">flip_l</span><span class="p">()</span></div><div class='line' id='LC193'><br/></div><div class='line' id='LC194'><span class="k">class</span> <span class="nc">FlipRightBullet</span><span class="p">(</span><span class="n">Bullet</span><span class="p">):</span></div><div class='line' id='LC195'>	<span class="sd">&quot;&quot;&quot;Bullet that will flip an enemy by it&#39;s right axis of symmetry.</span></div><div class='line' id='LC196'><span class="sd">	&quot;&quot;&quot;</span></div><div class='line' id='LC197'>	<span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC198'>		<span class="nb">super</span><span class="p">(</span><span class="n">FlipRightBullet</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="n">__init__</span><span class="p">(</span><span class="s">&#39;flip_right_bullet.png&#39;</span><span class="p">)</span></div><div class='line' id='LC199'><br/></div><div class='line' id='LC200'>	<span class="k">def</span> <span class="nf">on_hit</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">entity</span><span class="p">):</span></div><div class='line' id='LC201'>		<span class="k">if</span> <span class="n">entity</span><span class="o">.</span><span class="n">no_shield</span><span class="p">:</span></div><div class='line' id='LC202'>			<span class="n">entity</span><span class="o">.</span><span class="n">flip_r</span><span class="p">()</span></div><div class='line' id='LC203'><br/></div><div class='line' id='LC204'><span class="k">class</span> <span class="nc">KillBullet</span><span class="p">(</span><span class="n">Bullet</span><span class="p">):</span></div><div class='line' id='LC205'>	<span class="sd">&quot;&quot;&quot;Bullet that will kill an enemy that has its kill vertex exposed.</span></div><div class='line' id='LC206'><span class="sd">	&quot;&quot;&quot;</span></div><div class='line' id='LC207'>	<span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC208'>		<span class="nb">super</span><span class="p">(</span><span class="n">KillBullet</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="n">__init__</span><span class="p">(</span><span class="s">&#39;bullet.png&#39;</span><span class="p">)</span></div><div class='line' id='LC209'><br/></div><div class='line' id='LC210'>	<span class="k">def</span> <span class="nf">on_hit</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">entity</span><span class="p">):</span></div><div class='line' id='LC211'>		<span class="k">if</span> <span class="n">entity</span><span class="o">.</span><span class="n">kill_vertex</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span></div><div class='line' id='LC212'>			<span class="n">entity</span><span class="o">.</span><span class="n">kill</span><span class="p">()</span></div><div class='line' id='LC213'><br/></div><div class='line' id='LC214'><span class="k">class</span> <span class="nc">EnemyBullet</span><span class="p">(</span><span class="n">Bullet</span><span class="p">):</span></div><div class='line' id='LC215'>	<span class="sd">&quot;&quot;&quot;Enemies fire these. Go figure.</span></div><div class='line' id='LC216'><span class="sd">	&quot;&quot;&quot;</span></div><div class='line' id='LC217'>	<span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">dx</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span> <span class="n">dy</span><span class="o">=-</span><span class="mi">300</span><span class="p">):</span></div><div class='line' id='LC218'>		<span class="nb">super</span><span class="p">(</span><span class="n">EnemyBullet</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="n">__init__</span><span class="p">(</span><span class="s">&#39;enemy_bullet.png&#39;</span><span class="p">,</span> <span class="n">dx</span><span class="p">,</span> <span class="n">dy</span><span class="p">)</span></div><div class='line' id='LC219'><br/></div><div class='line' id='LC220'>	<span class="k">def</span> <span class="nf">on_hit</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">entity</span><span class="p">):</span></div><div class='line' id='LC221'>		<span class="c"># Player loses a life</span></div><div class='line' id='LC222'>		<span class="n">entity</span><span class="o">.</span><span class="n">lose_life</span><span class="p">()</span></div><div class='line' id='LC223'><br/></div><div class='line' id='LC224'><span class="k">class</span> <span class="nc">Player</span><span class="p">(</span><span class="n">cocos</span><span class="o">.</span><span class="n">sprite</span><span class="o">.</span><span class="n">Sprite</span><span class="p">):</span></div><div class='line' id='LC225'>	<span class="sd">&quot;&quot;&quot; Our courageous hero!</span></div><div class='line' id='LC226'><span class="sd">	&quot;&quot;&quot;</span></div><div class='line' id='LC227'>	<span class="c"># Fuck yeah bit masks!</span></div><div class='line' id='LC228'>	<span class="n">MOVE_LEFT</span> <span class="o">=</span> <span class="mi">1</span></div><div class='line' id='LC229'>	<span class="n">MOVE_RIGHT</span> <span class="o">=</span> <span class="mi">2</span></div><div class='line' id='LC230'>	<span class="n">MOVE_UP</span> <span class="o">=</span> <span class="mi">4</span></div><div class='line' id='LC231'>	<span class="n">MOVE_DOWN</span> <span class="o">=</span> <span class="mi">8</span></div><div class='line' id='LC232'><br/></div><div class='line' id='LC233'>	<span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC234'>		<span class="n">cocos</span><span class="o">.</span><span class="n">sprite</span><span class="o">.</span><span class="n">Sprite</span><span class="o">.</span><span class="n">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="s">&#39;ship.png&#39;</span><span class="p">)</span></div><div class='line' id='LC235'>		<span class="bp">self</span><span class="o">.</span><span class="n">move_mask</span> <span class="o">=</span> <span class="mi">0</span></div><div class='line' id='LC236'>		<span class="bp">self</span><span class="o">.</span><span class="n">speed</span> <span class="o">=</span> <span class="mi">500</span></div><div class='line' id='LC237'>		<span class="n">w</span><span class="p">,</span> <span class="n">h</span> <span class="o">=</span> <span class="n">director</span><span class="o">.</span><span class="n">get_window_size</span><span class="p">()</span></div><div class='line' id='LC238'>		<span class="bp">self</span><span class="o">.</span><span class="n">do</span><span class="p">(</span><span class="n">cocos</span><span class="o">.</span><span class="n">actions</span><span class="o">.</span><span class="n">move_actions</span><span class="o">.</span><span class="n">BoundedMove</span><span class="p">(</span><span class="n">w</span><span class="p">,</span> <span class="n">h</span><span class="p">))</span></div><div class='line' id='LC239'>		<span class="bp">self</span><span class="o">.</span><span class="n">velocity</span> <span class="o">=</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">0</span></div><div class='line' id='LC240'>		<span class="bp">self</span><span class="o">.</span><span class="n">no_clip</span> <span class="o">=</span> <span class="bp">False</span></div><div class='line' id='LC241'>		<span class="bp">self</span><span class="o">.</span><span class="n">_lives</span> <span class="o">=</span> <span class="mi">3</span></div><div class='line' id='LC242'>		<span class="bp">self</span><span class="o">.</span><span class="n">_score</span> <span class="o">=</span> <span class="mi">0</span></div><div class='line' id='LC243'>		<span class="bp">self</span><span class="o">.</span><span class="n">_chain</span> <span class="o">=</span> <span class="mi">0</span></div><div class='line' id='LC244'><br/></div><div class='line' id='LC245'>	<span class="k">def</span> <span class="nf">_get_chain</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC246'>		<span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_chain</span></div><div class='line' id='LC247'>	<span class="k">def</span> <span class="nf">_set_chain</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">chain</span><span class="p">):</span></div><div class='line' id='LC248'>		<span class="bp">self</span><span class="o">.</span><span class="n">_chain</span> <span class="o">=</span> <span class="n">chain</span></div><div class='line' id='LC249'>		<span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_chain</span> <span class="o">==</span> <span class="mi">9</span><span class="p">:</span></div><div class='line' id='LC250'>			<span class="bp">self</span><span class="o">.</span><span class="n">lives</span> <span class="o">+=</span> <span class="mi">1</span></div><div class='line' id='LC251'>			<span class="bp">self</span><span class="o">.</span><span class="n">_chain</span> <span class="o">=</span> <span class="mi">0</span></div><div class='line' id='LC252'>		<span class="bp">self</span><span class="o">.</span><span class="n">dispatch_event</span><span class="p">(</span><span class="s">&#39;on_chain_change&#39;</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_chain</span><span class="p">)</span></div><div class='line' id='LC253'>	<span class="n">chain</span> <span class="o">=</span> <span class="nb">property</span><span class="p">(</span><span class="n">_get_chain</span><span class="p">,</span> <span class="k">lambda</span> <span class="bp">self</span><span class="p">,</span><span class="n">chain</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_set_chain</span><span class="p">(</span><span class="n">chain</span><span class="p">))</span></div><div class='line' id='LC254'><br/></div><div class='line' id='LC255'>	<span class="k">def</span> <span class="nf">_get_lives</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC256'>		<span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_lives</span></div><div class='line' id='LC257'>	<span class="k">def</span> <span class="nf">_set_lives</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">lives</span><span class="p">):</span></div><div class='line' id='LC258'>		<span class="bp">self</span><span class="o">.</span><span class="n">_lives</span><span class="o">=</span> <span class="n">lives</span></div><div class='line' id='LC259'>		<span class="bp">self</span><span class="o">.</span><span class="n">dispatch_event</span><span class="p">(</span><span class="s">&#39;on_lives_change&#39;</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_lives</span><span class="p">)</span></div><div class='line' id='LC260'>	<span class="n">lives</span> <span class="o">=</span> <span class="nb">property</span><span class="p">(</span><span class="n">_get_lives</span><span class="p">,</span> <span class="k">lambda</span> <span class="bp">self</span><span class="p">,</span><span class="n">lives</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_set_lives</span><span class="p">(</span><span class="n">lives</span><span class="p">))</span></div><div class='line' id='LC261'><br/></div><div class='line' id='LC262'>	<span class="k">def</span> <span class="nf">_get_score</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC263'>		<span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_score</span></div><div class='line' id='LC264'>	<span class="k">def</span> <span class="nf">_set_score</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">score</span><span class="p">):</span></div><div class='line' id='LC265'>		<span class="bp">self</span><span class="o">.</span><span class="n">_score</span> <span class="o">=</span> <span class="n">score</span></div><div class='line' id='LC266'>		<span class="bp">self</span><span class="o">.</span><span class="n">dispatch_event</span><span class="p">(</span><span class="s">&#39;on_score_change&#39;</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_score</span><span class="p">)</span></div><div class='line' id='LC267'>	<span class="n">score</span> <span class="o">=</span> <span class="nb">property</span><span class="p">(</span><span class="n">_get_score</span><span class="p">,</span> <span class="k">lambda</span> <span class="bp">self</span><span class="p">,</span><span class="n">score</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_set_score</span><span class="p">(</span><span class="n">score</span><span class="p">))</span></div><div class='line' id='LC268'><br/></div><div class='line' id='LC269'>	<span class="k">def</span> <span class="nf">move</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">direction</span><span class="p">):</span></div><div class='line' id='LC270'>		<span class="bp">self</span><span class="o">.</span><span class="n">move_mask</span> <span class="o">|=</span> <span class="n">direction</span></div><div class='line' id='LC271'>		<span class="bp">self</span><span class="o">.</span><span class="n">update_velocity</span><span class="p">()</span></div><div class='line' id='LC272'><br/></div><div class='line' id='LC273'>	<span class="k">def</span> <span class="nf">stop_move</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">direction</span><span class="p">):</span></div><div class='line' id='LC274'>		<span class="bp">self</span><span class="o">.</span><span class="n">move_mask</span> <span class="o">&amp;=</span> <span class="o">~</span><span class="n">direction</span></div><div class='line' id='LC275'>		<span class="bp">self</span><span class="o">.</span><span class="n">update_velocity</span><span class="p">()</span></div><div class='line' id='LC276'><br/></div><div class='line' id='LC277'>	<span class="k">def</span> <span class="nf">fire</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">bullet</span><span class="p">):</span></div><div class='line' id='LC278'>		<span class="c"># The player cannot fire when no_clip is on</span></div><div class='line' id='LC279'>		<span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">no_clip</span><span class="p">:</span></div><div class='line' id='LC280'>			<span class="n">bullet</span><span class="o">.</span><span class="n">position</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">position</span></div><div class='line' id='LC281'>			<span class="bp">self</span><span class="o">.</span><span class="n">dispatch_event</span><span class="p">(</span><span class="s">&#39;on_player_fire&#39;</span><span class="p">,</span> <span class="n">bullet</span><span class="p">)</span></div><div class='line' id='LC282'><br/></div><div class='line' id='LC283'>	<span class="k">def</span> <span class="nf">update_velocity</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC284'>		<span class="n">dx</span> <span class="o">=</span> <span class="mi">0</span></div><div class='line' id='LC285'>		<span class="n">dy</span> <span class="o">=</span> <span class="mi">0</span></div><div class='line' id='LC286'><br/></div><div class='line' id='LC287'>		<span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">move_mask</span> <span class="o">&amp;</span> <span class="bp">self</span><span class="o">.</span><span class="n">MOVE_LEFT</span><span class="p">:</span></div><div class='line' id='LC288'>			<span class="n">dx</span> <span class="o">=</span> <span class="o">-</span><span class="bp">self</span><span class="o">.</span><span class="n">speed</span></div><div class='line' id='LC289'>		<span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">move_mask</span> <span class="o">&amp;</span> <span class="bp">self</span><span class="o">.</span><span class="n">MOVE_RIGHT</span><span class="p">:</span></div><div class='line' id='LC290'>			<span class="n">dx</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">speed</span></div><div class='line' id='LC291'>		<span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">move_mask</span> <span class="o">&amp;</span> <span class="bp">self</span><span class="o">.</span><span class="n">MOVE_UP</span><span class="p">:</span></div><div class='line' id='LC292'>			<span class="n">dy</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">speed</span></div><div class='line' id='LC293'>		<span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">move_mask</span> <span class="o">&amp;</span> <span class="bp">self</span><span class="o">.</span><span class="n">MOVE_DOWN</span><span class="p">:</span></div><div class='line' id='LC294'>			<span class="n">dy</span> <span class="o">=</span> <span class="o">-</span><span class="bp">self</span><span class="o">.</span><span class="n">speed</span></div><div class='line' id='LC295'><br/></div><div class='line' id='LC296'>		<span class="bp">self</span><span class="o">.</span><span class="n">velocity</span> <span class="o">=</span> <span class="p">(</span><span class="n">dx</span><span class="p">,</span> <span class="n">dy</span><span class="p">)</span></div><div class='line' id='LC297'><br/></div><div class='line' id='LC298'>	<span class="k">def</span> <span class="nf">lose_life</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC299'>		<span class="k">def</span> <span class="nf">func</span><span class="p">():</span></div><div class='line' id='LC300'>			<span class="bp">self</span><span class="o">.</span><span class="n">no_clip</span> <span class="o">=</span> <span class="bp">False</span></div><div class='line' id='LC301'>		<span class="bp">self</span><span class="o">.</span><span class="n">no_clip</span> <span class="o">=</span> <span class="bp">True</span></div><div class='line' id='LC302'>		<span class="bp">self</span><span class="o">.</span><span class="n">do</span><span class="p">(</span><span class="n">cocos</span><span class="o">.</span><span class="n">actions</span><span class="o">.</span><span class="n">Blink</span><span class="p">(</span><span class="mi">20</span><span class="p">,</span> <span class="mi">3</span><span class="p">)</span> <span class="o">+</span> <span class="n">cocos</span><span class="o">.</span><span class="n">actions</span><span class="o">.</span><span class="n">CallFunc</span><span class="p">(</span><span class="n">func</span><span class="p">))</span></div><div class='line' id='LC303'>		<span class="bp">self</span><span class="o">.</span><span class="n">lives</span> <span class="o">-=</span> <span class="mi">1</span></div><div class='line' id='LC304'>		<span class="bp">self</span><span class="o">.</span><span class="n">dispatch_event</span><span class="p">(</span><span class="s">&#39;on_lose_life&#39;</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">lives</span><span class="p">)</span></div><div class='line' id='LC305'><br/></div><div class='line' id='LC306'>	<span class="k">def</span> <span class="nf">on_hit</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC307'>		<span class="bp">self</span><span class="o">.</span><span class="n">lose_life</span><span class="p">()</span></div><div class='line' id='LC308'><br/></div><div class='line' id='LC309'><span class="n">Player</span><span class="o">.</span><span class="n">register_event_type</span><span class="p">(</span><span class="s">&#39;on_lose_life&#39;</span><span class="p">)</span></div><div class='line' id='LC310'><span class="n">Player</span><span class="o">.</span><span class="n">register_event_type</span><span class="p">(</span><span class="s">&#39;on_chain_change&#39;</span><span class="p">)</span></div><div class='line' id='LC311'><span class="n">Player</span><span class="o">.</span><span class="n">register_event_type</span><span class="p">(</span><span class="s">&#39;on_lives_change&#39;</span><span class="p">)</span></div><div class='line' id='LC312'><span class="n">Player</span><span class="o">.</span><span class="n">register_event_type</span><span class="p">(</span><span class="s">&#39;on_score_change&#39;</span><span class="p">)</span></div><div class='line' id='LC313'><span class="n">Player</span><span class="o">.</span><span class="n">register_event_type</span><span class="p">(</span><span class="s">&#39;on_player_fire&#39;</span><span class="p">)</span></div><div class='line' id='LC314'><br/></div><div class='line' id='LC315'><span class="k">class</span> <span class="nc">EnemyWeapon</span><span class="p">(</span><span class="nb">object</span><span class="p">):</span></div><div class='line' id='LC316'>	<span class="sd">&quot;&quot;&quot;Controls the pattern and rate with which the enemy fires bullets</span></div><div class='line' id='LC317'><span class="sd">	&quot;&quot;&quot;</span></div><div class='line' id='LC318'>	<span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">enemy</span><span class="p">,</span> <span class="n">interval</span><span class="p">):</span></div><div class='line' id='LC319'>		<span class="bp">self</span><span class="o">.</span><span class="n">enemy</span> <span class="o">=</span> <span class="n">enemy</span></div><div class='line' id='LC320'>		<span class="n">action</span> <span class="o">=</span> <span class="n">Repeat</span><span class="p">(</span><span class="n">Delay</span><span class="p">(</span><span class="mi">2</span><span class="p">)</span> <span class="o">+</span> <span class="p">(</span><span class="n">CallFunc</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">fire</span><span class="p">)</span> <span class="o">+</span> <span class="n">Delay</span><span class="p">(</span><span class="o">.</span><span class="mi">2</span><span class="p">))</span> <span class="o">*</span> <span class="mi">3</span><span class="p">)</span></div><div class='line' id='LC321'>		<span class="bp">self</span><span class="o">.</span><span class="n">enemy</span><span class="o">.</span><span class="n">do</span><span class="p">(</span><span class="n">action</span><span class="p">)</span></div><div class='line' id='LC322'><br/></div><div class='line' id='LC323'>	<span class="k">def</span> <span class="nf">fire</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC324'>		<span class="k">pass</span></div><div class='line' id='LC325'><br/></div><div class='line' id='LC326'><span class="k">class</span> <span class="nc">BasicEnemyWeapon</span><span class="p">(</span><span class="n">EnemyWeapon</span><span class="p">):</span></div><div class='line' id='LC327'>	<span class="sd">&quot;&quot;&quot;Fires bullets straight down</span></div><div class='line' id='LC328'><span class="sd">	&quot;&quot;&quot;</span></div><div class='line' id='LC329'>	<span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">enemy</span><span class="p">,</span> <span class="n">interval</span><span class="p">):</span></div><div class='line' id='LC330'>		<span class="nb">super</span><span class="p">(</span><span class="n">BasicEnemyWeapon</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="n">__init__</span><span class="p">(</span><span class="n">enemy</span><span class="p">,</span> <span class="n">interval</span><span class="p">)</span></div><div class='line' id='LC331'><br/></div><div class='line' id='LC332'>	<span class="k">def</span> <span class="nf">fire</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC333'>		<span class="n">bullet</span> <span class="o">=</span> <span class="n">EnemyBullet</span><span class="p">()</span></div><div class='line' id='LC334'>		<span class="n">bullet</span><span class="o">.</span><span class="n">position</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">enemy</span><span class="o">.</span><span class="n">position</span></div><div class='line' id='LC335'>		<span class="bp">self</span><span class="o">.</span><span class="n">enemy</span><span class="o">.</span><span class="n">dispatch_event</span><span class="p">(</span><span class="s">&#39;on_enemy_fire&#39;</span><span class="p">,</span> <span class="n">bullet</span><span class="p">)</span></div><div class='line' id='LC336'><br/></div><div class='line' id='LC337'><span class="k">class</span> <span class="nc">FanEnemyWeapon</span><span class="p">(</span><span class="n">EnemyWeapon</span><span class="p">):</span></div><div class='line' id='LC338'>	<span class="sd">&quot;&quot;&quot;Fires 3 streams of bullets straight down, and at a 45 degree to the left and right of the enemy&#39;s center x coordinate.</span></div><div class='line' id='LC339'><span class="sd">	&quot;&quot;&quot;</span></div><div class='line' id='LC340'>	<span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">enemy</span><span class="p">,</span> <span class="n">interval</span><span class="p">):</span></div><div class='line' id='LC341'>		<span class="nb">super</span><span class="p">(</span><span class="n">FanEnemyWeapon</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="n">__init__</span><span class="p">(</span><span class="n">enemy</span><span class="p">,</span> <span class="n">interval</span><span class="p">)</span></div><div class='line' id='LC342'>		<span class="bp">self</span><span class="o">.</span><span class="n">speed</span> <span class="o">=</span> <span class="mi">300</span></div><div class='line' id='LC343'><br/></div><div class='line' id='LC344'>	<span class="k">def</span> <span class="nf">fire</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC345'>		<span class="n">bullet</span> <span class="o">=</span> <span class="n">EnemyBullet</span><span class="p">(</span><span class="n">dy</span><span class="o">=-</span><span class="bp">self</span><span class="o">.</span><span class="n">speed</span><span class="p">)</span></div><div class='line' id='LC346'>		<span class="n">bullet</span><span class="o">.</span><span class="n">position</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">enemy</span><span class="o">.</span><span class="n">position</span></div><div class='line' id='LC347'>		<span class="bp">self</span><span class="o">.</span><span class="n">enemy</span><span class="o">.</span><span class="n">dispatch_event</span><span class="p">(</span><span class="s">&#39;on_enemy_fire&#39;</span><span class="p">,</span> <span class="n">bullet</span><span class="p">)</span></div><div class='line' id='LC348'>		<span class="n">bullet</span> <span class="o">=</span> <span class="n">EnemyBullet</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">speed</span><span class="p">,</span> <span class="o">-</span><span class="bp">self</span><span class="o">.</span><span class="n">speed</span><span class="p">)</span></div><div class='line' id='LC349'>		<span class="n">bullet</span><span class="o">.</span><span class="n">position</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">enemy</span><span class="o">.</span><span class="n">position</span></div><div class='line' id='LC350'>		<span class="bp">self</span><span class="o">.</span><span class="n">enemy</span><span class="o">.</span><span class="n">dispatch_event</span><span class="p">(</span><span class="s">&#39;on_enemy_fire&#39;</span><span class="p">,</span> <span class="n">bullet</span><span class="p">)</span></div><div class='line' id='LC351'>		<span class="n">bullet</span> <span class="o">=</span> <span class="n">EnemyBullet</span><span class="p">(</span><span class="o">-</span><span class="bp">self</span><span class="o">.</span><span class="n">speed</span><span class="p">,</span> <span class="o">-</span><span class="bp">self</span><span class="o">.</span><span class="n">speed</span><span class="p">)</span></div><div class='line' id='LC352'>		<span class="n">bullet</span><span class="o">.</span><span class="n">position</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">enemy</span><span class="o">.</span><span class="n">position</span></div><div class='line' id='LC353'>		<span class="bp">self</span><span class="o">.</span><span class="n">enemy</span><span class="o">.</span><span class="n">dispatch_event</span><span class="p">(</span><span class="s">&#39;on_enemy_fire&#39;</span><span class="p">,</span> <span class="n">bullet</span><span class="p">)</span></div><div class='line' id='LC354'><br/></div><div class='line' id='LC355'><span class="k">class</span> <span class="nc">EnemyPolygon</span><span class="p">(</span><span class="n">cocos</span><span class="o">.</span><span class="n">cocosnode</span><span class="o">.</span><span class="n">CocosNode</span><span class="p">,</span> <span class="n">pyglet</span><span class="o">.</span><span class="n">event</span><span class="o">.</span><span class="n">EventDispatcher</span><span class="p">):</span></div><div class='line' id='LC356'>	<span class="sd">&quot;&quot;&quot;Our polygonal adversary.</span></div><div class='line' id='LC357'><span class="sd">	&quot;&quot;&quot;</span></div><div class='line' id='LC358'><br/></div><div class='line' id='LC359'>	<span class="c"># Transformation constants for tracking last transformation applied</span></div><div class='line' id='LC360'>	<span class="n">ROTATE_CW</span> <span class="o">=</span> <span class="mi">1</span>	</div><div class='line' id='LC361'>	<span class="n">ROTATE_CCW</span> <span class="o">=</span> <span class="mi">2</span></div><div class='line' id='LC362'>	<span class="n">FLIP_L</span> <span class="o">=</span> <span class="mi">3</span></div><div class='line' id='LC363'>	<span class="n">FLIP_R</span> <span class="o">=</span> <span class="mi">4</span></div><div class='line' id='LC364'><br/></div><div class='line' id='LC365'>	<span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">num_vertices</span><span class="p">,</span> <span class="n">kill_vertex</span><span class="p">,</span> <span class="n">radius</span><span class="o">=</span><span class="mi">30</span><span class="p">,</span> <span class="n">image_file</span><span class="o">=</span><span class="s">&#39;enemy.png&#39;</span><span class="p">):</span></div><div class='line' id='LC366'>		<span class="c">#super(EnemyPolygon, self).__init__()</span></div><div class='line' id='LC367'>		<span class="n">cocos</span><span class="o">.</span><span class="n">cocosnode</span><span class="o">.</span><span class="n">CocosNode</span><span class="o">.</span><span class="n">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span></div><div class='line' id='LC368'>		<span class="n">pyglet</span><span class="o">.</span><span class="n">event</span><span class="o">.</span><span class="n">EventDispatcher</span><span class="o">.</span><span class="n">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span></div><div class='line' id='LC369'>		<span class="bp">self</span><span class="o">.</span><span class="n">num_vertices</span> <span class="o">=</span> <span class="n">num_vertices</span></div><div class='line' id='LC370'>		<span class="c"># Maximum number of transforms to expose a kill vertex in the worst case is floor(n / 2)</span></div><div class='line' id='LC371'>		<span class="c"># We&#39;re dealing with ints so no need to floor the value</span></div><div class='line' id='LC372'>		<span class="bp">self</span><span class="o">.</span><span class="n">max_hits</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">num_vertices</span> <span class="o">/</span> <span class="mi">2</span></div><div class='line' id='LC373'>		<span class="bp">self</span><span class="o">.</span><span class="n">radius</span> <span class="o">=</span> <span class="n">radius</span></div><div class='line' id='LC374'>		<span class="c"># Sprites that give a visual cue as to whether the kill vertex is exposed or not.</span></div><div class='line' id='LC375'>		<span class="bp">self</span><span class="o">.</span><span class="n">no</span> <span class="o">=</span> <span class="n">cocos</span><span class="o">.</span><span class="n">sprite</span><span class="o">.</span><span class="n">Sprite</span><span class="p">(</span><span class="s">&#39;no.png&#39;</span><span class="p">)</span></div><div class='line' id='LC376'>		<span class="bp">self</span><span class="o">.</span><span class="n">yes</span> <span class="o">=</span> <span class="n">cocos</span><span class="o">.</span><span class="n">sprite</span><span class="o">.</span><span class="n">Sprite</span><span class="p">(</span><span class="s">&#39;yes.png&#39;</span><span class="p">)</span></div><div class='line' id='LC377'>		<span class="c"># Enemy sprite</span></div><div class='line' id='LC378'>		<span class="c"># TODO: This will be customized on a per-enemy basis</span></div><div class='line' id='LC379'>		<span class="bp">self</span><span class="o">.</span><span class="n">sprite</span> <span class="o">=</span> <span class="n">cocos</span><span class="o">.</span><span class="n">sprite</span><span class="o">.</span><span class="n">Sprite</span><span class="p">(</span><span class="n">image_file</span><span class="p">)</span></div><div class='line' id='LC380'>		<span class="bp">self</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">sprite</span><span class="p">)</span></div><div class='line' id='LC381'>		<span class="c"># Assign the kill vertex to a non-downward vertex. The polygon&#39;s</span></div><div class='line' id='LC382'>		<span class="c"># downward vertex is zero, and the rest are numbered</span></div><div class='line' id='LC383'>		<span class="c"># incrementally counter-clockwise from the downward vertex.</span></div><div class='line' id='LC384'>		<span class="bp">self</span><span class="o">.</span><span class="n">kill_vertex</span> <span class="o">=</span> <span class="n">kill_vertex</span></div><div class='line' id='LC385'>		<span class="bp">self</span><span class="o">.</span><span class="n">update_sprites</span><span class="p">()</span></div><div class='line' id='LC386'>		<span class="c"># weapon</span></div><div class='line' id='LC387'>		<span class="bp">self</span><span class="o">.</span><span class="n">weapon</span> <span class="o">=</span> <span class="bp">None</span></div><div class='line' id='LC388'>		<span class="c"># Last transformation applied to this enemy</span></div><div class='line' id='LC389'>		<span class="bp">self</span><span class="o">.</span><span class="n">last_transform</span> <span class="o">=</span> <span class="mi">0</span></div><div class='line' id='LC390'>		<span class="c"># Enemy shield - activated when player mistransforms</span></div><div class='line' id='LC391'>		<span class="bp">self</span><span class="o">.</span><span class="n">no_shield</span> <span class="o">=</span> <span class="bp">True</span></div><div class='line' id='LC392'>		<span class="c"># Counts the amount of transformation bullets that have hit.</span></div><div class='line' id='LC393'>		<span class="bp">self</span><span class="o">.</span><span class="n">num_transforms</span> <span class="o">=</span> <span class="mi">0</span></div><div class='line' id='LC394'><br/></div><div class='line' id='LC395'>	<span class="k">def</span> <span class="nf">get_rect</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC396'>		<span class="n">rect</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">sprite</span><span class="o">.</span><span class="n">get_rect</span><span class="p">()</span></div><div class='line' id='LC397'>		<span class="n">rect</span><span class="o">.</span><span class="n">center</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">position</span></div><div class='line' id='LC398'>		<span class="k">return</span> <span class="n">rect</span></div><div class='line' id='LC399'><br/></div><div class='line' id='LC400'>	<span class="k">def</span> <span class="nf">update_sprites</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC401'>		<span class="sd">&quot;&quot;&quot;Sets the correct sprites based upon the kill vertex.</span></div><div class='line' id='LC402'><span class="sd">		&quot;&quot;&quot;</span></div><div class='line' id='LC403'>		<span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">kill_vertex</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span></div><div class='line' id='LC404'>			<span class="c"># This is a bit of a hack... it&#39;s just not pretty. It works, though.</span></div><div class='line' id='LC405'>			<span class="c"># Catch element not found exceptions</span></div><div class='line' id='LC406'>			<span class="k">try</span><span class="p">:</span></div><div class='line' id='LC407'>				<span class="bp">self</span><span class="o">.</span><span class="n">remove</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">no</span><span class="p">)</span></div><div class='line' id='LC408'>			<span class="k">except</span><span class="p">:</span></div><div class='line' id='LC409'>				<span class="k">pass</span></div><div class='line' id='LC410'>			<span class="bp">self</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">yes</span><span class="p">)</span></div><div class='line' id='LC411'>			<span class="n">angle</span> <span class="o">=</span> <span class="mi">2</span> <span class="o">*</span> <span class="n">math</span><span class="o">.</span><span class="n">pi</span> <span class="o">*</span> <span class="bp">self</span><span class="o">.</span><span class="n">kill_vertex</span> <span class="o">/</span> <span class="bp">self</span><span class="o">.</span><span class="n">num_vertices</span> <span class="o">-</span> <span class="n">math</span><span class="o">.</span><span class="n">pi</span> <span class="o">/</span> <span class="mi">2</span></div><div class='line' id='LC412'>			<span class="bp">self</span><span class="o">.</span><span class="n">yes</span><span class="o">.</span><span class="n">position</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">radius</span> <span class="o">*</span> <span class="n">math</span><span class="o">.</span><span class="n">cos</span><span class="p">(</span><span class="n">angle</span><span class="p">),</span> <span class="bp">self</span><span class="o">.</span><span class="n">radius</span> <span class="o">*</span> <span class="n">math</span><span class="o">.</span><span class="n">sin</span><span class="p">(</span><span class="n">angle</span><span class="p">)</span></div><div class='line' id='LC413'>		<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC414'>			<span class="k">try</span><span class="p">:</span></div><div class='line' id='LC415'>				<span class="bp">self</span><span class="o">.</span><span class="n">remove</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">yes</span><span class="p">)</span></div><div class='line' id='LC416'>			<span class="k">except</span><span class="p">:</span></div><div class='line' id='LC417'>				<span class="k">pass</span></div><div class='line' id='LC418'>			<span class="bp">self</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">no</span><span class="p">)</span></div><div class='line' id='LC419'>			<span class="n">angle</span> <span class="o">=</span> <span class="mi">2</span> <span class="o">*</span> <span class="n">math</span><span class="o">.</span><span class="n">pi</span> <span class="o">*</span> <span class="bp">self</span><span class="o">.</span><span class="n">kill_vertex</span> <span class="o">/</span> <span class="bp">self</span><span class="o">.</span><span class="n">num_vertices</span> <span class="o">-</span> <span class="n">math</span><span class="o">.</span><span class="n">pi</span> <span class="o">/</span> <span class="mi">2</span></div><div class='line' id='LC420'>			<span class="bp">self</span><span class="o">.</span><span class="n">no</span><span class="o">.</span><span class="n">position</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">radius</span> <span class="o">*</span> <span class="n">math</span><span class="o">.</span><span class="n">cos</span><span class="p">(</span><span class="n">angle</span><span class="p">),</span> <span class="bp">self</span><span class="o">.</span><span class="n">radius</span> <span class="o">*</span> <span class="n">math</span><span class="o">.</span><span class="n">sin</span><span class="p">(</span><span class="n">angle</span><span class="p">)</span></div><div class='line' id='LC421'><br/></div><div class='line' id='LC422'>	<span class="c"># Rotate clockwise</span></div><div class='line' id='LC423'>	<span class="k">def</span> <span class="nf">rotate_cw</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC424'>		<span class="bp">self</span><span class="o">.</span><span class="n">num_transforms</span> <span class="o">+=</span> <span class="mi">1</span></div><div class='line' id='LC425'>		<span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">last_transform</span> <span class="o">!=</span> <span class="bp">self</span><span class="o">.</span><span class="n">ROTATE_CW</span><span class="p">:</span></div><div class='line' id='LC426'>			<span class="bp">self</span><span class="o">.</span><span class="n">kill_vertex</span> <span class="o">=</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">kill_vertex</span> <span class="o">-</span> <span class="mi">1</span><span class="p">)</span> <span class="o">%</span> <span class="bp">self</span><span class="o">.</span><span class="n">num_vertices</span></div><div class='line' id='LC427'>			<span class="bp">self</span><span class="o">.</span><span class="n">update_sprites</span><span class="p">()</span></div><div class='line' id='LC428'>			<span class="bp">self</span><span class="o">.</span><span class="n">last_transform</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">ROTATE_CW</span></div><div class='line' id='LC429'>		<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC430'>			<span class="bp">self</span><span class="o">.</span><span class="n">bad_transform</span><span class="p">()</span></div><div class='line' id='LC431'><br/></div><div class='line' id='LC432'>	<span class="c"># Rotate counter-clockwise</span></div><div class='line' id='LC433'>	<span class="k">def</span> <span class="nf">rotate_ccw</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC434'>		<span class="bp">self</span><span class="o">.</span><span class="n">num_transforms</span> <span class="o">+=</span> <span class="mi">1</span></div><div class='line' id='LC435'>		<span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">last_transform</span> <span class="o">!=</span> <span class="bp">self</span><span class="o">.</span><span class="n">ROTATE_CCW</span><span class="p">:</span></div><div class='line' id='LC436'>			<span class="bp">self</span><span class="o">.</span><span class="n">kill_vertex</span> <span class="o">=</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">kill_vertex</span> <span class="o">+</span> <span class="mi">1</span><span class="p">)</span> <span class="o">%</span> <span class="bp">self</span><span class="o">.</span><span class="n">num_vertices</span></div><div class='line' id='LC437'>			<span class="bp">self</span><span class="o">.</span><span class="n">update_sprites</span><span class="p">()</span></div><div class='line' id='LC438'>			<span class="bp">self</span><span class="o">.</span><span class="n">last_transform</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">ROTATE_CCW</span></div><div class='line' id='LC439'>		<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC440'>			<span class="bp">self</span><span class="o">.</span><span class="n">bad_transform</span><span class="p">()</span></div><div class='line' id='LC441'><br/></div><div class='line' id='LC442'>	<span class="c"># Flip about line of symmetry passing through the side directly</span></div><div class='line' id='LC443'>	<span class="c"># to the left of the downward vertex</span></div><div class='line' id='LC444'>	<span class="k">def</span> <span class="nf">flip_l</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC445'>		<span class="bp">self</span><span class="o">.</span><span class="n">num_transforms</span> <span class="o">+=</span> <span class="mi">1</span></div><div class='line' id='LC446'>		<span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">last_transform</span> <span class="o">!=</span> <span class="bp">self</span><span class="o">.</span><span class="n">FLIP_L</span><span class="p">:</span></div><div class='line' id='LC447'>			<span class="bp">self</span><span class="o">.</span><span class="n">kill_vertex</span> <span class="o">=</span> <span class="p">(</span><span class="o">-</span><span class="bp">self</span><span class="o">.</span><span class="n">kill_vertex</span> <span class="o">-</span> <span class="mi">1</span><span class="p">)</span> <span class="o">%</span> <span class="bp">self</span><span class="o">.</span><span class="n">num_vertices</span></div><div class='line' id='LC448'>			<span class="bp">self</span><span class="o">.</span><span class="n">update_sprites</span><span class="p">()</span></div><div class='line' id='LC449'>			<span class="bp">self</span><span class="o">.</span><span class="n">last_transform</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">FLIP_L</span></div><div class='line' id='LC450'>		<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC451'>			<span class="bp">self</span><span class="o">.</span><span class="n">bad_transform</span><span class="p">()</span></div><div class='line' id='LC452'><br/></div><div class='line' id='LC453'>	<span class="c"># Flip about line of symmetry passing through the side directly</span></div><div class='line' id='LC454'>	<span class="c"># to the right of the downward vertex</span></div><div class='line' id='LC455'>	<span class="k">def</span> <span class="nf">flip_r</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC456'>		<span class="bp">self</span><span class="o">.</span><span class="n">num_transforms</span> <span class="o">+=</span> <span class="mi">1</span></div><div class='line' id='LC457'>		<span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">last_transform</span> <span class="o">!=</span> <span class="bp">self</span><span class="o">.</span><span class="n">FLIP_R</span><span class="p">:</span></div><div class='line' id='LC458'>			<span class="bp">self</span><span class="o">.</span><span class="n">kill_vertex</span> <span class="o">=</span> <span class="p">(</span><span class="o">-</span><span class="bp">self</span><span class="o">.</span><span class="n">kill_vertex</span> <span class="o">+</span> <span class="mi">1</span><span class="p">)</span> <span class="o">%</span> <span class="bp">self</span><span class="o">.</span><span class="n">num_vertices</span></div><div class='line' id='LC459'>			<span class="bp">self</span><span class="o">.</span><span class="n">update_sprites</span><span class="p">()</span></div><div class='line' id='LC460'>			<span class="bp">self</span><span class="o">.</span><span class="n">last_transform</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">FLIP_R</span></div><div class='line' id='LC461'>		<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC462'>			<span class="bp">self</span><span class="o">.</span><span class="n">bad_transform</span><span class="p">()</span></div><div class='line' id='LC463'><br/></div><div class='line' id='LC464'>	<span class="k">def</span> <span class="nf">bad_transform</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC465'>		<span class="k">def</span> <span class="nf">shield_up</span><span class="p">():</span></div><div class='line' id='LC466'>			<span class="bp">self</span><span class="o">.</span><span class="n">no_shield</span> <span class="o">=</span> <span class="bp">False</span></div><div class='line' id='LC467'>		<span class="k">def</span> <span class="nf">shield_down</span><span class="p">():</span></div><div class='line' id='LC468'>			<span class="bp">self</span><span class="o">.</span><span class="n">no_shield</span> <span class="o">=</span> <span class="bp">True</span></div><div class='line' id='LC469'>		<span class="bp">self</span><span class="o">.</span><span class="n">do</span><span class="p">(</span><span class="n">cocos</span><span class="o">.</span><span class="n">actions</span><span class="o">.</span><span class="n">CallFunc</span><span class="p">(</span><span class="n">shield_up</span><span class="p">)</span> <span class="o">+</span> <span class="n">Delay</span><span class="p">(</span><span class="mi">3</span><span class="p">)</span> <span class="o">+</span> <span class="n">cocos</span><span class="o">.</span><span class="n">actions</span><span class="o">.</span><span class="n">CallFunc</span><span class="p">(</span><span class="n">shield_down</span><span class="p">))</span></div><div class='line' id='LC470'>		<span class="bp">self</span><span class="o">.</span><span class="n">dispatch_event</span><span class="p">(</span><span class="s">&#39;on_bad_transform&#39;</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span></div><div class='line' id='LC471'><br/></div><div class='line' id='LC472'>	<span class="c"># Manage the death of the enemy polygon</span></div><div class='line' id='LC473'>	<span class="k">def</span> <span class="nf">kill</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC474'>		<span class="bp">self</span><span class="o">.</span><span class="n">dispatch_event</span><span class="p">(</span><span class="s">&#39;on_enemy_death&#39;</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span></div><div class='line' id='LC475'><br/></div><div class='line' id='LC476'>	<span class="k">def</span> <span class="nf">draw</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC477'>		<span class="n">glPushMatrix</span><span class="p">()</span></div><div class='line' id='LC478'>		<span class="bp">self</span><span class="o">.</span><span class="n">transform</span><span class="p">()</span></div><div class='line' id='LC479'>		<span class="c"># Draw polygon</span></div><div class='line' id='LC480'>		<span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">no_shield</span><span class="p">:</span></div><div class='line' id='LC481'>			<span class="n">glColor3f</span><span class="p">(</span><span class="mf">0.0</span><span class="p">,</span> <span class="mf">0.0</span><span class="p">,</span> <span class="mf">1.0</span><span class="p">)</span></div><div class='line' id='LC482'>		<span class="k">elif</span> <span class="bp">self</span><span class="o">.</span><span class="n">kill_vertex</span> <span class="o">!=</span> <span class="mi">0</span><span class="p">:</span></div><div class='line' id='LC483'>			<span class="n">glColor3f</span><span class="p">(</span><span class="mf">1.0</span><span class="p">,</span> <span class="mf">0.0</span><span class="p">,</span> <span class="mf">0.0</span><span class="p">)</span> <span class="c"># red color</span></div><div class='line' id='LC484'>		<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC485'>			<span class="n">glColor3f</span><span class="p">(</span><span class="mf">0.0</span><span class="p">,</span> <span class="mf">1.0</span><span class="p">,</span> <span class="mf">0.0</span><span class="p">)</span></div><div class='line' id='LC486'>		<span class="n">glLineWidth</span><span class="p">(</span><span class="mi">3</span><span class="p">)</span></div><div class='line' id='LC487'>		<span class="n">glEnable</span><span class="p">(</span><span class="n">GL_LINE_SMOOTH</span><span class="p">)</span></div><div class='line' id='LC488'>		<span class="c"># Construct polygon by its vertices, starting with the</span></div><div class='line' id='LC489'>		<span class="c"># downward vertex and working counter-clockwise</span></div><div class='line' id='LC490'>		<span class="c"># TODO: Put this stuff in a vertex buffer</span></div><div class='line' id='LC491'>		<span class="n">glBegin</span><span class="p">(</span><span class="n">GL_LINE_LOOP</span><span class="p">)</span></div><div class='line' id='LC492'>		<span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">num_vertices</span><span class="p">):</span></div><div class='line' id='LC493'>			<span class="n">angle</span> <span class="o">=</span> <span class="mi">2</span> <span class="o">*</span> <span class="n">math</span><span class="o">.</span><span class="n">pi</span> <span class="o">*</span> <span class="n">i</span> <span class="o">/</span> <span class="bp">self</span><span class="o">.</span><span class="n">num_vertices</span> <span class="o">-</span> <span class="n">math</span><span class="o">.</span><span class="n">pi</span> <span class="o">/</span> <span class="mi">2</span></div><div class='line' id='LC494'>			<span class="n">glVertex2f</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">radius</span> <span class="o">*</span> <span class="n">math</span><span class="o">.</span><span class="n">cos</span><span class="p">(</span><span class="n">angle</span><span class="p">),</span> <span class="bp">self</span><span class="o">.</span><span class="n">radius</span> <span class="o">*</span> <span class="n">math</span><span class="o">.</span><span class="n">sin</span><span class="p">(</span><span class="n">angle</span><span class="p">))</span></div><div class='line' id='LC495'>		<span class="n">glEnd</span><span class="p">()</span></div><div class='line' id='LC496'>		<span class="n">glPopMatrix</span><span class="p">()</span></div><div class='line' id='LC497'><br/></div><div class='line' id='LC498'><span class="n">EnemyPolygon</span><span class="o">.</span><span class="n">register_event_type</span><span class="p">(</span><span class="s">&#39;on_enemy_fire&#39;</span><span class="p">)</span></div><div class='line' id='LC499'><span class="n">EnemyPolygon</span><span class="o">.</span><span class="n">register_event_type</span><span class="p">(</span><span class="s">&#39;on_enemy_death&#39;</span><span class="p">)</span></div><div class='line' id='LC500'><span class="n">EnemyPolygon</span><span class="o">.</span><span class="n">register_event_type</span><span class="p">(</span><span class="s">&#39;on_bad_transform&#39;</span><span class="p">)</span></div><div class='line' id='LC501'><br/></div></pre></div>
              
            
          </td>
        </tr>
      </table>
    
  </div>


          </div>
        </div>
      </div>
    </div>
  

  </div>


<div class="frame frame-loading" style="display:none;">
  <img src="https://d3nwyuy0nl342s.cloudfront.net/images/modules/ajax/big_spinner_336699.gif" height="32" width="32">
</div>

    </div>
  
      
    </div>

    <div id="footer" class="clearfix">
      <div class="site">
        <div class="sponsor">
          <a href="http://www.rackspace.com" class="logo">
            <img alt="Dedicated Server" height="36" src="https://d3nwyuy0nl342s.cloudfront.net/images/modules/footer/rackspace_logo.png?v2" width="38" />
          </a>
          Powered by the <a href="http://www.rackspace.com ">Dedicated
          Servers</a> and<br/> <a href="http://www.rackspacecloud.com">Cloud
          Computing</a> of Rackspace Hosting<span>&reg;</span>
        </div>

        <ul class="links">
          <li class="blog"><a href="https://github.com/blog">Blog</a></li>
          <li><a href="/login/multipass?to=http%3A%2F%2Fsupport.github.com">Support</a></li>
          <li><a href="https://github.com/training">Training</a></li>
          <li><a href="http://jobs.github.com">Job Board</a></li>
          <li><a href="http://shop.github.com">Shop</a></li>
          <li><a href="https://github.com/contact">Contact</a></li>
          <li><a href="http://develop.github.com">API</a></li>
          <li><a href="http://status.github.com">Status</a></li>
        </ul>
        <ul class="sosueme">
          <li class="main">&copy; 2011 <span id="_rrt" title="0.06556s from fe1.rs.github.com">GitHub</span> Inc. All rights reserved.</li>
          <li><a href="/site/terms">Terms of Service</a></li>
          <li><a href="/site/privacy">Privacy</a></li>
          <li><a href="https://github.com/security">Security</a></li>
        </ul>
      </div>
    </div><!-- /#footer -->

    
      
      
        <!-- current locale:  -->
        <div class="locales instapaper_ignore readability-footer">
          <div class="site">

            <ul class="choices clearfix limited-locales">
              <li><span class="current">English</span></li>
              
                  <li><a rel="nofollow" href="?locale=de">Deutsch</a></li>
              
                  <li><a rel="nofollow" href="?locale=fr">Français</a></li>
              
                  <li><a rel="nofollow" href="?locale=ja">日本語</a></li>
              
                  <li><a rel="nofollow" href="?locale=pt-BR">Português (BR)</a></li>
              
                  <li><a rel="nofollow" href="?locale=ru">Русский</a></li>
              
                  <li><a rel="nofollow" href="?locale=zh">中文</a></li>
              
              <li class="all"><a href="#" class="minibutton btn-forward js-all-locales"><span><span class="icon"></span>See all available languages</span></a></li>
            </ul>

            <div class="all-locales clearfix">
              <h3>Your current locale selection: <strong>English</strong>. Choose another?</h3>
              
              
                <ul class="choices">
                  
                      <li><a rel="nofollow" href="?locale=en">English</a></li>
                  
                      <li><a rel="nofollow" href="?locale=af">Afrikaans</a></li>
                  
                      <li><a rel="nofollow" href="?locale=ca">Català</a></li>
                  
                      <li><a rel="nofollow" href="?locale=cs">Čeština</a></li>
                  
                      <li><a rel="nofollow" href="?locale=de">Deutsch</a></li>
                  
                </ul>
              
                <ul class="choices">
                  
                      <li><a rel="nofollow" href="?locale=es">Español</a></li>
                  
                      <li><a rel="nofollow" href="?locale=fr">Français</a></li>
                  
                      <li><a rel="nofollow" href="?locale=hr">Hrvatski</a></li>
                  
                      <li><a rel="nofollow" href="?locale=hu">Magyar</a></li>
                  
                      <li><a rel="nofollow" href="?locale=id">Indonesia</a></li>
                  
                </ul>
              
                <ul class="choices">
                  
                      <li><a rel="nofollow" href="?locale=it">Italiano</a></li>
                  
                      <li><a rel="nofollow" href="?locale=ja">日本語</a></li>
                  
                      <li><a rel="nofollow" href="?locale=nl">Nederlands</a></li>
                  
                      <li><a rel="nofollow" href="?locale=no">Norsk</a></li>
                  
                      <li><a rel="nofollow" href="?locale=pl">Polski</a></li>
                  
                </ul>
              
                <ul class="choices">
                  
                      <li><a rel="nofollow" href="?locale=pt-BR">Português (BR)</a></li>
                  
                      <li><a rel="nofollow" href="?locale=ru">Русский</a></li>
                  
                      <li><a rel="nofollow" href="?locale=sr">Српски</a></li>
                  
                      <li><a rel="nofollow" href="?locale=sv">Svenska</a></li>
                  
                      <li><a rel="nofollow" href="?locale=zh">中文</a></li>
                  
                </ul>
              
            </div>

          </div>
          <div class="fade"></div>
        </div>
      
    

    <script>window._auth_token = "89efacf64308c6a640927f40e257c40abe2da29f"</script>
    

<div id="keyboard_shortcuts_pane" class="instapaper_ignore readability-extra" style="display:none">
  <h2>Keyboard Shortcuts <small><a href="#" class="js-see-all-keyboard-shortcuts">(see all)</a></small></h2>

  <div class="columns threecols">
    <div class="column first">
      <h3>Site wide shortcuts</h3>
      <dl class="keyboard-mappings">
        <dt>s</dt>
        <dd>Focus site search</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>?</dt>
        <dd>Bring up this help dialog</dd>
      </dl>
    </div><!-- /.column.first -->

    <div class="column middle" style='display:none'>
      <h3>Commit list</h3>
      <dl class="keyboard-mappings">
        <dt>j</dt>
        <dd>Move selected down</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>k</dt>
        <dd>Move selected up</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>t</dt>
        <dd>Open tree</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>p</dt>
        <dd>Open parent</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>c <em>or</em> o <em>or</em> enter</dt>
        <dd>Open commit</dd>
      </dl>
    </div><!-- /.column.first -->

    <div class="column last" style='display:none'>
      <h3>Pull request list</h3>
      <dl class="keyboard-mappings">
        <dt>j</dt>
        <dd>Move selected down</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>k</dt>
        <dd>Move selected up</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>o <em>or</em> enter</dt>
        <dd>Open issue</dd>
      </dl>
    </div><!-- /.columns.last -->

  </div><!-- /.columns.equacols -->

  <div style='display:none'>
    <div class="rule"></div>

    <h3>Issues</h3>

    <div class="columns threecols">
      <div class="column first">
        <dl class="keyboard-mappings">
          <dt>j</dt>
          <dd>Move selected down</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>k</dt>
          <dd>Move selected up</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>x</dt>
          <dd>Toggle select target</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>o <em>or</em> enter</dt>
          <dd>Open issue</dd>
        </dl>
      </div><!-- /.column.first -->
      <div class="column middle">
        <dl class="keyboard-mappings">
          <dt>I</dt>
          <dd>Mark selected as read</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>U</dt>
          <dd>Mark selected as unread</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>e</dt>
          <dd>Close selected</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>y</dt>
          <dd>Remove selected from view</dd>
        </dl>
      </div><!-- /.column.middle -->
      <div class="column last">
        <dl class="keyboard-mappings">
          <dt>c</dt>
          <dd>Create issue</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>l</dt>
          <dd>Create label</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>i</dt>
          <dd>Back to inbox</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>u</dt>
          <dd>Back to issues</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>/</dt>
          <dd>Focus issues search</dd>
        </dl>
      </div>
    </div>
  </div>

  <div style='display:none'>
    <div class="rule"></div>

    <h3>Network Graph</h3>
    <div class="columns equacols">
      <div class="column first">
        <dl class="keyboard-mappings">
          <dt><span class="badmono">←</span> <em>or</em> h</dt>
          <dd>Scroll left</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt><span class="badmono">→</span> <em>or</em> l</dt>
          <dd>Scroll right</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt><span class="badmono">↑</span> <em>or</em> k</dt>
          <dd>Scroll up</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt><span class="badmono">↓</span> <em>or</em> j</dt>
          <dd>Scroll down</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>t</dt>
          <dd>Toggle visibility of head labels</dd>
        </dl>
      </div><!-- /.column.first -->
      <div class="column last">
        <dl class="keyboard-mappings">
          <dt>shift <span class="badmono">←</span> <em>or</em> shift h</dt>
          <dd>Scroll all the way left</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>shift <span class="badmono">→</span> <em>or</em> shift l</dt>
          <dd>Scroll all the way right</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>shift <span class="badmono">↑</span> <em>or</em> shift k</dt>
          <dd>Scroll all the way up</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>shift <span class="badmono">↓</span> <em>or</em> shift j</dt>
          <dd>Scroll all the way down</dd>
        </dl>
      </div><!-- /.column.last -->
    </div>
  </div>

  <div >
    <div class="rule"></div>

    <h3>Source Code Browsing</h3>
    <div class="columns threecols">
      <div class="column first">
        <dl class="keyboard-mappings">
          <dt>t</dt>
          <dd>Activates the file finder</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>l</dt>
          <dd>Jump to line</dd>
        </dl>
      </div>
    </div>
  </div>

</div>
    

    <!--[if IE 8]>
    <script type="text/javascript" charset="utf-8">
      $(document.body).addClass("ie8")
    </script>
    <![endif]-->

    <!--[if IE 7]>
    <script type="text/javascript" charset="utf-8">
      $(document.body).addClass("ie7")
    </script>
    <![endif]-->

    
    <script type='text/javascript'></script>
    
  </body>
</html>

=======
import pyglet
from pyglet.gl import *
import cocos
from cocos.director import director
from cocos.actions import *
from cocos.particle_systems import Explosion
import math
import random
from collections import deque
import level

class GameModel(pyglet.event.EventDispatcher):
	def __init__(self):
		super(GameModel, self).__init__()

		self.levels = deque()
		self.current_level = None
		# Testing wave class
		def make_action(enemy):
			path = level.create_enemy_path(enemy, enemy.x + 100, enemy.y - 150, level.BEND_UP)
			action = Bezier(path, 5)
			return Repeat(action + MoveBy((-100, 150)))
		def make_weapon(enemy):
			return BasicEnemyWeapon(enemy, 1)
		enemy1 = level.WaveEnemy(3, 1, make_action, make_weapon)
		enemy2 = level.WaveEnemy(5, 3, make_action, make_weapon)
		wave0 = level.Wave(level.horizontalLayout(600), [enemy1, enemy1, enemy1, enemy1])
		wave1 = level.Wave(level.horizontalLayout(500), [enemy1, enemy2, enemy1, enemy2])
		wave2 = level.Wave(level.horizontalLayout(400), [enemy2, enemy2, enemy2, enemy2])
		level1 = level.Level([wave0, wave1, wave2])
		#wave3 = level.Wave([(6, None), (6, None), (6, None)])
		#wave4 = level.Wave([(7, None), (8, None)])
		#level2 = level.Level([wave3, wave4])
		self.levels.append(level1)
		#self.levels.append(level2)
			
		# Add the player
		self.player = Player()
		self.player.position = 400, 300
		# Node for player bullets
		self.player_bullets = cocos.batch.BatchNode()
		# Node for enemy bullets
		self.enemy_bullets = cocos.batch.BatchNode()
		# Node for particles
		self.particles = cocos.cocosnode.CocosNode()

		# Register player event listeners
		self.player.push_handlers(self)

	def next_level(self):
		# No levels left? WE HAVE A WINRAR!
		if len(self.levels) == 0:
			import getvictory
			director.replace(getvictory.get_scene(self.player.score))
			return

		self.current_level = self.levels.popleft()
		self.dispatch_event('on_new_level')
		self.current_level.push_handlers(self)
		self.current_level.next_wave()
	
	def on_new_wave(self, wave):
		for e in wave.get_children():
			e.push_handlers(self)
	
	def on_level_complete(self):
		self.next_level()

	def on_lose_life(self, lives):
		# Make an explosion particle effect
		p = Explosion()
		p.position = self.player.position
		self.particles.add(p)
		# Reset the player to the center of the screen
		w, h = director.get_window_size()
		self.player.position = w/2, h/2
		# If the player is out of lives it's game over.
		if lives == 0:
			import getgameover
			director.replace(getgameover.get_scene(self.player.score))

	def on_bad_transform(self, enemy):
		self.player.chain = 0
	
	def on_enemy_death(self, enemy):
		self.player.chain += 1
		max_transforms = enemy.num_vertices / 2
		# Points multiplier
		# Full points awarded for taking n/2 or less transformations to kill enemy
		# Points reduced with each additional hit
		multiplier = max_transforms / float(max(max_transforms, enemy.num_transforms))
		self.player.score += enemy.num_vertices * 10 * multiplier
		p = Explosion()
		p.position = enemy.position
		self.particles.add(p)

	def on_player_fire(self, bullet):
		self.player_bullets.add(bullet)

	def on_enemy_fire(self, bullet):
		self.enemy_bullets.add(bullet)

	def step(self, dt):
		"""Called every frame, this method updates objects that have time dependent calculations to perform.
		"""
		# Some inefficient naive collision detection
		for b in self.player_bullets.get_children():
			for e in self.current_level.current_wave.get_children():
				if b.get_rect().intersects(e.get_rect()):
					b.on_hit(e)
					self.player_bullets.remove(b)
					return
		if not self.player.no_clip:
			for e in self.current_level.current_wave.get_children():
				if self.player.get_rect().intersects(e.get_rect()):
					self.player.on_hit()
					return
			for b in self.enemy_bullets.get_children():
				if b.get_rect().intersects(self.player.get_rect()):
					b.on_hit(self.player)
					self.enemy_bullets.remove(b)
					return

GameModel.register_event_type('on_new_level')

class RemoveBoundedMove(cocos.actions.move_actions.Move):
	"""Move the target but remove it from the parent when it reaches certain bounds.
	Modified from the cocos2d sources to fit the needed purpose.
	This action is used for bullets.
	"""
	def init(self, width, height):
		self.width, self.height = width, height

	def step(self, dt):
		super(RemoveBoundedMove, self).step(dt)
		x, y = self.target.position
		w, h = self.target.width, self.target.height
		# Out of bounds, remove the node from the parent
		if x > self.width + w/2 or x < 0 - w/2 or y > self.height + h/2 or y < 0 - h/2:
			self.target.parent.remove(self.target)

		self.target.position = (x, y)

class Bullet(cocos.sprite.Sprite):
	"""Provides the functionality to create differing bullet types by using event handlers.
	"""
	def __init__(self, image_file, dx=0, dy=500):
		"""dx and dy parameters set the bullet speed and vector.
		"""
		super(Bullet, self).__init__(image_file)
		self.velocity = dx, dy
		w, h = director.get_window_size()
		self.do(RemoveBoundedMove(w, h))
	
	def step(self, dt):
		self.x += self.dx * dt
		self.y += self.dy * dt

	def on_hit(self, entity):
		"""Hit event handler.
		Customize this to do what you want the bullet to do.
		"""
		pass

class RotateCWBullet(Bullet):
	"""Bullet that will rotate an enemy's kill vertex one 'step' clockwise.
	"""
	def __init__(self):
		super(RotateCWBullet, self).__init__('rotate_cw_bullet.png')
	
	def on_hit(self, entity):
		if entity.no_shield:
			entity.rotate_cw()

class RotateCCWBullet(Bullet):
	"""Bullet that will rotate an enemy's kill vertex one 'step' counter clockwise.
	"""
	def __init__(self):
		super(RotateCCWBullet, self).__init__('rotate_ccw_bullet.png')
	
	def on_hit(self, entity):
		if entity.no_shield:
			entity.rotate_ccw()
		
class FlipLeftBullet(Bullet):
	"""Bullet that will flip an enemy by it's left axis of symmetry.
	"""
	def __init__(self):
		super(FlipLeftBullet, self).__init__('flip_left_bullet.png')
	
	def on_hit(self, entity):
		if entity.no_shield:
			entity.flip_l()

class FlipRightBullet(Bullet):
	"""Bullet that will flip an enemy by it's right axis of symmetry.
	"""
	def __init__(self):
		super(FlipRightBullet, self).__init__('flip_right_bullet.png')
	
	def on_hit(self, entity):
		if entity.no_shield:
			entity.flip_r()

class KillBullet(Bullet):
	"""Bullet that will kill an enemy that has its kill vertex exposed.
	"""
	def __init__(self):
		super(KillBullet, self).__init__('bullet.png')
	
	def on_hit(self, entity):
		if entity.kill_vertex == 0:
			entity.kill()

class EnemyBullet(Bullet):
	"""Enemies fire these. Go figure.
	"""
	def __init__(self, dx=0, dy=-300):
		super(EnemyBullet, self).__init__('enemy_bullet.png', dx, dy)
	
	def on_hit(self, entity):
		# Player loses a life
		entity.lose_life()

class Player(cocos.sprite.Sprite):
	""" Our courageous hero!
	"""
	# Fuck yeah bit masks!
	MOVE_LEFT = 1
	MOVE_RIGHT = 2
	MOVE_UP = 4
	MOVE_DOWN = 8

	def __init__(self):
		cocos.sprite.Sprite.__init__(self, 'ship.png')
		self.move_mask = 0
		self.speed = 500
		w, h = director.get_window_size()
		self.do(cocos.actions.move_actions.BoundedMove(w, h))
		self.velocity = 0, 0
		self.no_clip = False
		self._lives = 3
		self._score = 0
		self._chain = 0
	
	def _get_chain(self):
		return self._chain
	def _set_chain(self, chain):
		self._chain = chain
		if self._chain == 9:
			self.lives += 1
			self._chain = 0
		self.dispatch_event('on_chain_change', self._chain)
	chain = property(_get_chain, lambda self,chain: self._set_chain(chain))

	def _get_lives(self):
		return self._lives
	def _set_lives(self, lives):
		self._lives= lives
		self.dispatch_event('on_lives_change', self._lives)
	lives = property(_get_lives, lambda self,lives: self._set_lives(lives))

	def _get_score(self):
		return self._score
	def _set_score(self, score):
		self._score = score
		self.dispatch_event('on_score_change', self._score)
	score = property(_get_score, lambda self,score: self._set_score(score))

	def move(self, direction):
		self.move_mask |= direction
		self.update_velocity()
	
	def stop_move(self, direction):
		self.move_mask &= ~direction
		self.update_velocity()
	
	def fire(self, bullet):
		# The player cannot fire when no_clip is on
		if not self.no_clip:
			bullet.position = self.position
			self.dispatch_event('on_player_fire', bullet)
	
	def update_velocity(self):
		dx = 0
		dy = 0

		if self.move_mask & self.MOVE_LEFT:
			dx = -self.speed
		if self.move_mask & self.MOVE_RIGHT:
			dx = self.speed
		if self.move_mask & self.MOVE_UP:
			dy = self.speed
		if self.move_mask & self.MOVE_DOWN:
			dy = -self.speed

		self.velocity = (dx, dy)
	
	def lose_life(self):
		def func():
			self.no_clip = False
		self.no_clip = True
		self.do(cocos.actions.Blink(20, 3) + cocos.actions.CallFunc(func))
		self.lives -= 1
		self.dispatch_event('on_lose_life', self.lives)
	
	def on_hit(self):
		self.lose_life()

Player.register_event_type('on_lose_life')
Player.register_event_type('on_chain_change')
Player.register_event_type('on_lives_change')
Player.register_event_type('on_score_change')
Player.register_event_type('on_player_fire')

class EnemyWeapon(object):
	"""Controls the pattern and rate with which the enemy fires bullets
	"""
	def __init__(self, enemy, interval):
		self.enemy = enemy
		action = Repeat(Delay(2) + (CallFunc(self.fire) + Delay(.2)) * 3)
		self.enemy.do(action)
	
	def fire(self):
		pass

class BasicEnemyWeapon(EnemyWeapon):
	"""Fires bullets straight down
	"""
	def __init__(self, enemy, interval):
		super(BasicEnemyWeapon, self).__init__(enemy, interval)
	
	def fire(self):
		bullet = EnemyBullet()
		bullet.position = self.enemy.position
		self.enemy.dispatch_event('on_enemy_fire', bullet)

class FanEnemyWeapon(EnemyWeapon):
	"""Fires 3 streams of bullets straight down, and at a 45 degree to the left and right of the enemy's center x coordinate.
	"""
	def __init__(self, enemy, interval):
		super(FanEnemyWeapon, self).__init__(enemy, interval)
		self.speed = 300
	
	def fire(self):
		bullet = EnemyBullet(dy=-self.speed)
		bullet.position = self.enemy.position
		self.enemy.dispatch_event('on_enemy_fire', bullet)
		bullet = EnemyBullet(self.speed, -self.speed)
		bullet.position = self.enemy.position
		self.enemy.dispatch_event('on_enemy_fire', bullet)
		bullet = EnemyBullet(-self.speed, -self.speed)
		bullet.position = self.enemy.position
		self.enemy.dispatch_event('on_enemy_fire', bullet)

class EnemyPolygon(cocos.cocosnode.CocosNode, pyglet.event.EventDispatcher):
	"""Our polygonal adversary.
	"""

	# Transformation constants for tracking last transformation applied
	ROTATE_CW = 1	
	ROTATE_CCW = 2
	FLIP_L = 3
	FLIP_R = 4

	def __init__(self, num_vertices, kill_vertex, radius=30, image_file='enemy.png'):
		#super(EnemyPolygon, self).__init__()
		cocos.cocosnode.CocosNode.__init__(self)
		pyglet.event.EventDispatcher.__init__(self)
		self.num_vertices = num_vertices
		# Maximum number of transforms to expose a kill vertex in the worst case is floor(n / 2)
		# We're dealing with ints so no need to floor the value
		self.max_hits = self.num_vertices / 2
		self.radius = radius
		# Sprites that give a visual cue as to whether the kill vertex is exposed or not.
		self.no = cocos.sprite.Sprite('no.png')
		self.yes = cocos.sprite.Sprite('yes.png')
		# Enemy sprite
		# TODO: This will be customized on a per-enemy basis
		self.sprite = cocos.sprite.Sprite(image_file)
		self.add(self.sprite)
		# Assign the kill vertex to a non-downward vertex. The polygon's
		# downward vertex is zero, and the rest are numbered
		# incrementally counter-clockwise from the downward vertex.
		self.kill_vertex = kill_vertex
		self.update_sprites()
		# weapon
		self.weapon = None
		# Last transformation applied to this enemy
		self.last_transform = 0
		# Enemy shield - activated when player mistransforms
		self.no_shield = True
		# Counts the amount of transformation bullets that have hit.
		self.num_transforms = 0
	
	def get_rect(self):
		rect = self.sprite.get_rect()
		rect.center = self.position
		return rect
	
	def update_sprites(self):
		"""Sets the correct sprites based upon the kill vertex.
		"""
		if self.kill_vertex == 0:
			# This is a bit of a hack... it's just not pretty. It works, though.
			# Catch element not found exceptions
			try:
				self.remove(self.no)
			except:
				pass
			self.add(self.yes)
			angle = 2 * math.pi * self.kill_vertex / self.num_vertices - math.pi / 2
			self.yes.position = self.radius * math.cos(angle), self.radius * math.sin(angle)
		else:
			try:
				self.remove(self.yes)
			except:
				pass
			self.add(self.no)
			angle = 2 * math.pi * self.kill_vertex / self.num_vertices - math.pi / 2
			self.no.position = self.radius * math.cos(angle), self.radius * math.sin(angle)

	# Rotate clockwise
	def rotate_cw(self):
		self.num_transforms += 1
		if self.last_transform != self.ROTATE_CW:
			self.kill_vertex = (self.kill_vertex - 1) % self.num_vertices
			self.update_sprites()
			self.last_transform = self.ROTATE_CW
		else:
			self.bad_transform()

	# Rotate counter-clockwise
	def rotate_ccw(self):
		self.num_transforms += 1
		if self.last_transform != self.ROTATE_CCW:
			self.kill_vertex = (self.kill_vertex + 1) % self.num_vertices
			self.update_sprites()
			self.last_transform = self.ROTATE_CCW
		else:
			self.bad_transform()

	# Flip about line of symmetry passing through the side directly
	# to the left of the downward vertex
	def flip_l(self):
		self.num_transforms += 1
		if self.last_transform != self.FLIP_L:
			self.kill_vertex = (-self.kill_vertex - 1) % self.num_vertices
			self.update_sprites()
			self.last_transform = self.FLIP_L
		else:
			self.bad_transform()

	# Flip about line of symmetry passing through the side directly
	# to the right of the downward vertex
	def flip_r(self):
		self.num_transforms += 1
		if self.last_transform != self.FLIP_R:
			self.kill_vertex = (-self.kill_vertex + 1) % self.num_vertices
			self.update_sprites()
			self.last_transform = self.FLIP_R
		else:
			self.bad_transform()

	def bad_transform(self):
		def shield_up():
			self.no_shield = False
		def shield_down():
			self.no_shield = True
		self.do(cocos.actions.CallFunc(shield_up) + Delay(3) + cocos.actions.CallFunc(shield_down))
		self.dispatch_event('on_bad_transform', self)

	# Manage the death of the enemy polygon
	def kill(self):
		self.dispatch_event('on_enemy_death', self)

	def draw(self):
		glPushMatrix()
		self.transform()
		# Draw polygon
		if not self.no_shield:
			glColor3f(0.0, 0.0, 1.0)
		elif self.kill_vertex != 0:
			glColor3f(1.0, 0.0, 0.0) # red color
		else:
			glColor3f(0.0, 1.0, 0.0)
		glLineWidth(3)
		glEnable(GL_LINE_SMOOTH)
		# Construct polygon by its vertices, starting with the
		# downward vertex and working counter-clockwise
		# TODO: Put this stuff in a vertex buffer
		glBegin(GL_LINE_LOOP)
		for i in range(self.num_vertices):
			angle = 2 * math.pi * i / self.num_vertices - math.pi / 2
			glVertex2f(self.radius * math.cos(angle), self.radius * math.sin(angle))
		glEnd()
		glPopMatrix()
	
EnemyPolygon.register_event_type('on_enemy_fire')
EnemyPolygon.register_event_type('on_enemy_death')
EnemyPolygon.register_event_type('on_bad_transform')
>>>>>>> upstream/master
