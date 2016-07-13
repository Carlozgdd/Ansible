<!DOCTYPE html>
<html lang='en'>
<head>
<meta charset='utf-8'>
<meta content='GitLab Community Edition' name='description'>
<title>
gen-orchestra-signature.py at master | 
GitLab
</title>
<link href="/assets/favicon-d6aa61c7c265900a7d4c45d3ac2b461f.ico" rel="shortcut icon" type="image/vnd.microsoft.icon" />
<link href="/assets/application-715bc4efac6b42deb84d495309f19f9a.css" media="all" rel="stylesheet" />
<link href="/assets/print-8597f8b497e02f892aa5a4b25d5a857b.css" media="print" rel="stylesheet" />
<script src="/assets/application-5ec1aeb4604cbfbeff836f956308b0ed.js"></script>
<meta content="authenticity_token" name="csrf-param" />
<meta content="dbVUpZ17FD78NRcLVTadqJrzF3oUMxwzEz1zrUjc+GY=" name="csrf-token" />
<script type="text/javascript">
//<![CDATA[
window.gon={};gon.default_issues_tracker="gitlab";gon.api_version="v3";gon.relative_url_root="";gon.default_avatar_url="http://gitlab.internal.travelsoft.fr/assets/no_avatar-fd406ccede8cb1881f20921c8bfa169b.png";gon.current_user_id=15;gon.api_token="1bR-ZcKeJjiNxzS95fY1";
//]]>
</script>
<meta content='width=device-width, initial-scale=1, maximum-scale=1' name='viewport'>
<meta content='#474D57' name='theme-color'>


</head>

<body class='ui_mars  project' data-page='projects:blob:show' data-project-id='27'>
<header class='navbar navbar-fixed-top navbar-gitlab'>
<div class='navbar-inner'>
<div class='container'>
<div class='app_logo'>
<a class="home has_bottom_tooltip" href="/" title="Dashboard"><img alt="Logo white" src="/assets/logo-white-0b53cd4ea06811d79b3acd486384e047.png" />
</a></div>
<h1 class='title'><span><a href="/groups/Exploit">Exploit</a> / <a href="/Exploit/signatureGenerator">signatureGenerator</a></span></h1>
<button class='navbar-toggle' data-target='.navbar-collapse' data-toggle='collapse' type='button'>
<span class='sr-only'>Toggle navigation</span>
<i class='fa fa-bars'></i>
</button>
<div class='navbar-collapse collapse'>
<ul class='nav navbar-nav'>
<li class='hidden-sm hidden-xs'>
<div class='search'>
<form accept-charset="UTF-8" action="/search" class="navbar-form pull-left" method="get"><div style="display:none"><input name="utf8" type="hidden" value="&#x2713;" /></div>
<input class="search-input" id="search" name="search" placeholder="Search in this project" type="search" />
<input id="group_id" name="group_id" type="hidden" />
<input id="project_id" name="project_id" type="hidden" value="27" />
<input id="search_code" name="search_code" type="hidden" value="true" />
<input id="repository_ref" name="repository_ref" type="hidden" value="master" />

<div class='search-autocomplete-opts hide' data-autocomplete-path='/search/autocomplete' data-autocomplete-project-id='27' data-autocomplete-project-ref='master'></div>
</form>

</div>
<script>
  $('.search-input').on('keyup', function(e) {
    if (e.keyCode == 27) {
      $('.search-input').blur()
    }
  })
</script>

</li>
<li class='visible-sm visible-xs'>
<a class="has_bottom_tooltip" data-original-title="Search area" href="/search" title="Search"><i class='fa fa-search'></i>
</a></li>
<li>
<a class="has_bottom_tooltip" data-original-title="Help" href="/help" title="Help"><i class='fa fa-question-circle'></i>
</a></li>
<li>
<a class="has_bottom_tooltip" data-original-title="Public area" href="/explore" title="Explore"><i class='fa fa-globe'></i>
</a></li>
<li>
<a class="has_bottom_tooltip" data-original-title="My snippets" href="/s/helene.hannedouche" title="My snippets"><i class='fa fa-clipboard'></i>
</a></li>
<li>
<a class="has_bottom_tooltip" data-original-title="New project" href="/projects/new" title="New project"><i class='fa fa-plus'></i>
</a></li>
<li>
<a class="has_bottom_tooltip" data-original-title="Profile settings&quot;" href="/profile" title="Profile settings"><i class='fa fa-user'></i>
</a></li>
<li>
<a class="has_bottom_tooltip" data-method="delete" data-original-title="Logout" href="/users/sign_out" rel="nofollow" title="Logout"><i class='fa fa-sign-out'></i>
</a></li>
<li class='hidden-xs'>
<a class="profile-pic has_bottom_tooltip" data-original-title="Your profile" href="/u/helene.hannedouche" id="profile-pic"><img alt="User activity" src="http://www.gravatar.com/avatar/318a1740b142a0f80dd05e28953a37ac?s=60&amp;d=identicon" />
</a></li>
</ul>
</div>
</div>
</div>
</header>


<script>
  GitLab.GfmAutoComplete.dataSource = "/Exploit/signatureGenerator/autocomplete_sources?type=NilClass&type_id=master%2Fgen-orchestra-signature.py"
  GitLab.GfmAutoComplete.setup();
</script>

<div class='page-sidebar-expanded page-with-sidebar'>

<div class='sidebar-wrapper'>
<ul class='project-navigation nav nav-sidebar'>
<li class="home"><a class="shortcuts-project" href="/Exploit/signatureGenerator" title="Project"><i class='fa fa-dashboard'></i>
<span>
Project
</span>
</a></li><li class="active"><a class="shortcuts-tree" href="/Exploit/signatureGenerator/tree/master" title="Files"><i class='fa fa-files-o'></i>
<span>
Files
</span>
</a></li><li class=""><a class="shortcuts-commits" href="/Exploit/signatureGenerator/commits/master" title="Commits"><i class='fa fa-history'></i>
<span>
Commits
</span>
</a></li><li class=""><a class="shortcuts-network" href="/Exploit/signatureGenerator/network/master" title="Network"><i class='fa fa-code-fork'></i>
<span>
Network
</span>
</a></li><li class=""><a class="shortcuts-graphs" href="/Exploit/signatureGenerator/graphs/master" title="Graphs"><i class='fa fa-area-chart'></i>
<span>
Graphs
</span>
</a></li><li class=""><a href="/Exploit/signatureGenerator/milestones" title="Milestones"><i class='fa fa-clock-o'></i>
<span>
Milestones
</span>
</a></li><li class=""><a class="shortcuts-issues" href="/Exploit/signatureGenerator/issues" title="Issues"><i class='fa fa-exclamation-circle'></i>
<span>
Issues
<span class='count issue_counter'>0</span>
</span>
</a></li><li class=""><a class="shortcuts-merge_requests" href="/Exploit/signatureGenerator/merge_requests" title="Merge Requests"><i class='fa fa-tasks'></i>
<span>
Merge Requests
<span class='count merge_counter'>0</span>
</span>
</a></li><li class=""><a href="/Exploit/signatureGenerator/labels" title="Labels"><i class='fa fa-tags'></i>
<span>
Labels
</span>
</a></li><li class=""><a class="shortcuts-wiki" href="/Exploit/signatureGenerator/wikis/home" title="Wiki"><i class='fa fa-book'></i>
<span>
Wiki
</span>
</a></li><li class="separate-item"><a class="stat-tab tab no-highlight" href="/Exploit/signatureGenerator/edit" title="Settings"><i class='fa fa-cogs'></i>
<span>
Settings
</span>
</a></li></ul>

<div class='collapse-nav'>
<a class="toggle-nav-collapse" href="#" title="Open/Close"><i class="fa fa-angle-left"></i></a>

</div>
</div>
<div class='content-wrapper'>
<div class='container-fluid'>
<div class='content'>
<div class='flash-container'>
</div>

<div class='clearfix'>
<div class='tree-ref-holder'>
<form accept-charset="UTF-8" action="/Exploit/signatureGenerator/refs/switch" class="project-refs-form" method="get"><div style="display:none"><input name="utf8" type="hidden" value="&#x2713;" /></div>
<select class="project-refs-select select2 select2-sm" id="ref" name="ref"><optgroup label="Branches"><option selected="selected" value="master">master</option></optgroup><optgroup label="Tags"></optgroup></select>
<input id="destination" name="destination" type="hidden" value="blob" />
<input id="path" name="path" type="hidden" value="gen-orchestra-signature.py" />
</form>


</div>
<div class='tree-holder' id='tree-holder'>
<ul class='breadcrumb repo-breadcrumb'>
<li>
<i class='fa fa-angle-right'></i>
<a href="/Exploit/signatureGenerator/tree/master">signatureGenerator
</a></li>
<li>
<a href="/Exploit/signatureGenerator/blob/master/gen-orchestra-signature.py"><strong>
gen-orchestra-signature.py
</strong>
</a></li>
</ul>
<ul class='blob-commit-info well hidden-xs'>
<li class='commit js-toggle-container'>
<div class='commit-row-title'>
<strong class='str-truncated'>
<a class="commit-row-message" href="/Exploit/signatureGenerator/commit/b78aba5a0c23927fcae67fbff687a2d7634c197a">Init project with script and template</a>
</strong>
<div class='pull-right'>
<a class="commit_short_id" href="/Exploit/signatureGenerator/commit/b78aba5a0c23927fcae67fbff687a2d7634c197a">b78aba5a</a>
</div>
<div class='notes_count'>
</div>
</div>
<div class='commit-row-info'>
<a class="commit-author-link has_tooltip" data-original-title="christophe.biguereau@orchestra.eu" href="/u/christophe.biguereau"><img alt="" class="avatar s24" src="http://gitlab.internal.travelsoft.fr/uploads/user/avatar/4/punisher_logo_by_woodnutiam-d48ro0d.jpg" width="24" /> <span class="commit-author-name">Christophe Biguereau</span></a>
authored
<div class='committed_ago'>
<time class='time_ago' data-placement='top' data-toggle='tooltip' datetime='2015-07-13T13:29:18Z' title='Jul 13, 2015 3:29pm'>2015-07-13 15:29:18 +0200</time>
<script>$('.time_ago').timeago().tooltip()</script>
 &nbsp;
</div>
<a class="pull-right" href="/Exploit/signatureGenerator/tree/b78aba5a0c23927fcae67fbff687a2d7634c197a">Browse Code »</a>
</div>
</li>

</ul>
<div class='tree-content-holder' id='tree-content-holder'>
<article class='file-holder'>
<div class='file-title'>
<i class='fa fa-file'></i>
<strong>
gen-orchestra-signature.py
</strong>
<small>
3.57 KB
</small>
<div class='file-actions hidden-xs'>
<div class='btn-group tree-btn-group'>
<a class="btn btn-small" href="/Exploit/signatureGenerator/edit/master/gen-orchestra-signature.py">Edit</a>
<a class="btn btn-sm" href="/Exploit/signatureGenerator/raw/master/gen-orchestra-signature.py" target="_blank">Raw</a>
<a class="btn btn-sm" href="/Exploit/signatureGenerator/blame/master/gen-orchestra-signature.py">Blame</a>
<a class="btn btn-sm" href="/Exploit/signatureGenerator/commits/master/gen-orchestra-signature.py">History</a>
<a class="btn btn-sm" href="/Exploit/signatureGenerator/blob/69c5b5416d0fdeb947d773d9b1289ae2f322f6cf/gen-orchestra-signature.py">Permalink</a>
</div>
<button class="remove-blob btn btn-sm btn-remove" data-target="#modal-remove-blob" data-toggle="modal" name="button" type="submit">Remove
</button>
</div>
</div>
<div class='file-content code'>
<div class='code file-content white'>
<div class='line-numbers'>
<a href="#L1" id="L1" rel="#L1"><i class='fa fa-link'></i>
1
</a><a href="#L2" id="L2" rel="#L2"><i class='fa fa-link'></i>
2
</a><a href="#L3" id="L3" rel="#L3"><i class='fa fa-link'></i>
3
</a><a href="#L4" id="L4" rel="#L4"><i class='fa fa-link'></i>
4
</a><a href="#L5" id="L5" rel="#L5"><i class='fa fa-link'></i>
5
</a><a href="#L6" id="L6" rel="#L6"><i class='fa fa-link'></i>
6
</a><a href="#L7" id="L7" rel="#L7"><i class='fa fa-link'></i>
7
</a><a href="#L8" id="L8" rel="#L8"><i class='fa fa-link'></i>
8
</a><a href="#L9" id="L9" rel="#L9"><i class='fa fa-link'></i>
9
</a><a href="#L10" id="L10" rel="#L10"><i class='fa fa-link'></i>
10
</a><a href="#L11" id="L11" rel="#L11"><i class='fa fa-link'></i>
11
</a><a href="#L12" id="L12" rel="#L12"><i class='fa fa-link'></i>
12
</a><a href="#L13" id="L13" rel="#L13"><i class='fa fa-link'></i>
13
</a><a href="#L14" id="L14" rel="#L14"><i class='fa fa-link'></i>
14
</a><a href="#L15" id="L15" rel="#L15"><i class='fa fa-link'></i>
15
</a><a href="#L16" id="L16" rel="#L16"><i class='fa fa-link'></i>
16
</a><a href="#L17" id="L17" rel="#L17"><i class='fa fa-link'></i>
17
</a><a href="#L18" id="L18" rel="#L18"><i class='fa fa-link'></i>
18
</a><a href="#L19" id="L19" rel="#L19"><i class='fa fa-link'></i>
19
</a><a href="#L20" id="L20" rel="#L20"><i class='fa fa-link'></i>
20
</a><a href="#L21" id="L21" rel="#L21"><i class='fa fa-link'></i>
21
</a><a href="#L22" id="L22" rel="#L22"><i class='fa fa-link'></i>
22
</a><a href="#L23" id="L23" rel="#L23"><i class='fa fa-link'></i>
23
</a><a href="#L24" id="L24" rel="#L24"><i class='fa fa-link'></i>
24
</a><a href="#L25" id="L25" rel="#L25"><i class='fa fa-link'></i>
25
</a><a href="#L26" id="L26" rel="#L26"><i class='fa fa-link'></i>
26
</a><a href="#L27" id="L27" rel="#L27"><i class='fa fa-link'></i>
27
</a><a href="#L28" id="L28" rel="#L28"><i class='fa fa-link'></i>
28
</a><a href="#L29" id="L29" rel="#L29"><i class='fa fa-link'></i>
29
</a><a href="#L30" id="L30" rel="#L30"><i class='fa fa-link'></i>
30
</a><a href="#L31" id="L31" rel="#L31"><i class='fa fa-link'></i>
31
</a><a href="#L32" id="L32" rel="#L32"><i class='fa fa-link'></i>
32
</a><a href="#L33" id="L33" rel="#L33"><i class='fa fa-link'></i>
33
</a><a href="#L34" id="L34" rel="#L34"><i class='fa fa-link'></i>
34
</a><a href="#L35" id="L35" rel="#L35"><i class='fa fa-link'></i>
35
</a><a href="#L36" id="L36" rel="#L36"><i class='fa fa-link'></i>
36
</a><a href="#L37" id="L37" rel="#L37"><i class='fa fa-link'></i>
37
</a><a href="#L38" id="L38" rel="#L38"><i class='fa fa-link'></i>
38
</a><a href="#L39" id="L39" rel="#L39"><i class='fa fa-link'></i>
39
</a><a href="#L40" id="L40" rel="#L40"><i class='fa fa-link'></i>
40
</a><a href="#L41" id="L41" rel="#L41"><i class='fa fa-link'></i>
41
</a><a href="#L42" id="L42" rel="#L42"><i class='fa fa-link'></i>
42
</a><a href="#L43" id="L43" rel="#L43"><i class='fa fa-link'></i>
43
</a><a href="#L44" id="L44" rel="#L44"><i class='fa fa-link'></i>
44
</a><a href="#L45" id="L45" rel="#L45"><i class='fa fa-link'></i>
45
</a><a href="#L46" id="L46" rel="#L46"><i class='fa fa-link'></i>
46
</a><a href="#L47" id="L47" rel="#L47"><i class='fa fa-link'></i>
47
</a><a href="#L48" id="L48" rel="#L48"><i class='fa fa-link'></i>
48
</a><a href="#L49" id="L49" rel="#L49"><i class='fa fa-link'></i>
49
</a><a href="#L50" id="L50" rel="#L50"><i class='fa fa-link'></i>
50
</a><a href="#L51" id="L51" rel="#L51"><i class='fa fa-link'></i>
51
</a><a href="#L52" id="L52" rel="#L52"><i class='fa fa-link'></i>
52
</a><a href="#L53" id="L53" rel="#L53"><i class='fa fa-link'></i>
53
</a><a href="#L54" id="L54" rel="#L54"><i class='fa fa-link'></i>
54
</a><a href="#L55" id="L55" rel="#L55"><i class='fa fa-link'></i>
55
</a><a href="#L56" id="L56" rel="#L56"><i class='fa fa-link'></i>
56
</a><a href="#L57" id="L57" rel="#L57"><i class='fa fa-link'></i>
57
</a><a href="#L58" id="L58" rel="#L58"><i class='fa fa-link'></i>
58
</a><a href="#L59" id="L59" rel="#L59"><i class='fa fa-link'></i>
59
</a><a href="#L60" id="L60" rel="#L60"><i class='fa fa-link'></i>
60
</a><a href="#L61" id="L61" rel="#L61"><i class='fa fa-link'></i>
61
</a><a href="#L62" id="L62" rel="#L62"><i class='fa fa-link'></i>
62
</a><a href="#L63" id="L63" rel="#L63"><i class='fa fa-link'></i>
63
</a><a href="#L64" id="L64" rel="#L64"><i class='fa fa-link'></i>
64
</a><a href="#L65" id="L65" rel="#L65"><i class='fa fa-link'></i>
65
</a><a href="#L66" id="L66" rel="#L66"><i class='fa fa-link'></i>
66
</a><a href="#L67" id="L67" rel="#L67"><i class='fa fa-link'></i>
67
</a><a href="#L68" id="L68" rel="#L68"><i class='fa fa-link'></i>
68
</a><a href="#L69" id="L69" rel="#L69"><i class='fa fa-link'></i>
69
</a><a href="#L70" id="L70" rel="#L70"><i class='fa fa-link'></i>
70
</a><a href="#L71" id="L71" rel="#L71"><i class='fa fa-link'></i>
71
</a><a href="#L72" id="L72" rel="#L72"><i class='fa fa-link'></i>
72
</a><a href="#L73" id="L73" rel="#L73"><i class='fa fa-link'></i>
73
</a><a href="#L74" id="L74" rel="#L74"><i class='fa fa-link'></i>
74
</a><a href="#L75" id="L75" rel="#L75"><i class='fa fa-link'></i>
75
</a><a href="#L76" id="L76" rel="#L76"><i class='fa fa-link'></i>
76
</a><a href="#L77" id="L77" rel="#L77"><i class='fa fa-link'></i>
77
</a><a href="#L78" id="L78" rel="#L78"><i class='fa fa-link'></i>
78
</a><a href="#L79" id="L79" rel="#L79"><i class='fa fa-link'></i>
79
</a><a href="#L80" id="L80" rel="#L80"><i class='fa fa-link'></i>
80
</a><a href="#L81" id="L81" rel="#L81"><i class='fa fa-link'></i>
81
</a><a href="#L82" id="L82" rel="#L82"><i class='fa fa-link'></i>
82
</a><a href="#L83" id="L83" rel="#L83"><i class='fa fa-link'></i>
83
</a><a href="#L84" id="L84" rel="#L84"><i class='fa fa-link'></i>
84
</a><a href="#L85" id="L85" rel="#L85"><i class='fa fa-link'></i>
85
</a><a href="#L86" id="L86" rel="#L86"><i class='fa fa-link'></i>
86
</a><a href="#L87" id="L87" rel="#L87"><i class='fa fa-link'></i>
87
</a><a href="#L88" id="L88" rel="#L88"><i class='fa fa-link'></i>
88
</a><a href="#L89" id="L89" rel="#L89"><i class='fa fa-link'></i>
89
</a><a href="#L90" id="L90" rel="#L90"><i class='fa fa-link'></i>
90
</a><a href="#L91" id="L91" rel="#L91"><i class='fa fa-link'></i>
91
</a><a href="#L92" id="L92" rel="#L92"><i class='fa fa-link'></i>
92
</a><a href="#L93" id="L93" rel="#L93"><i class='fa fa-link'></i>
93
</a><a href="#L94" id="L94" rel="#L94"><i class='fa fa-link'></i>
94
</a><a href="#L95" id="L95" rel="#L95"><i class='fa fa-link'></i>
95
</a><a href="#L96" id="L96" rel="#L96"><i class='fa fa-link'></i>
96
</a><a href="#L97" id="L97" rel="#L97"><i class='fa fa-link'></i>
97
</a><a href="#L98" id="L98" rel="#L98"><i class='fa fa-link'></i>
98
</a><a href="#L99" id="L99" rel="#L99"><i class='fa fa-link'></i>
99
</a><a href="#L100" id="L100" rel="#L100"><i class='fa fa-link'></i>
100
</a><a href="#L101" id="L101" rel="#L101"><i class='fa fa-link'></i>
101
</a><a href="#L102" id="L102" rel="#L102"><i class='fa fa-link'></i>
102
</a><a href="#L103" id="L103" rel="#L103"><i class='fa fa-link'></i>
103
</a><a href="#L104" id="L104" rel="#L104"><i class='fa fa-link'></i>
104
</a><a href="#L105" id="L105" rel="#L105"><i class='fa fa-link'></i>
105
</a><a href="#L106" id="L106" rel="#L106"><i class='fa fa-link'></i>
106
</a><a href="#L107" id="L107" rel="#L107"><i class='fa fa-link'></i>
107
</a><a href="#L108" id="L108" rel="#L108"><i class='fa fa-link'></i>
108
</a><a href="#L109" id="L109" rel="#L109"><i class='fa fa-link'></i>
109
</a><a href="#L110" id="L110" rel="#L110"><i class='fa fa-link'></i>
110
</a><a href="#L111" id="L111" rel="#L111"><i class='fa fa-link'></i>
111
</a><a href="#L112" id="L112" rel="#L112"><i class='fa fa-link'></i>
112
</a><a href="#L113" id="L113" rel="#L113"><i class='fa fa-link'></i>
113
</a><a href="#L114" id="L114" rel="#L114"><i class='fa fa-link'></i>
114
</a></div>
<pre class="code highlight"><code><span id="LC1" class="line"><span class="c">#!/usr/bin/python3</span></span>&#x000A;<span id="LC2" class="line"></span>&#x000A;<span id="LC3" class="line"><span class="c"># TODO: create html signature</span></span>&#x000A;<span id="LC4" class="line"><span class="c"># need:</span></span>&#x000A;<span id="LC5" class="line"><span class="c"># - Colorama</span></span>&#x000A;<span id="LC6" class="line"><span class="c"># - Jinja2 ( version 2.5 )</span></span>&#x000A;<span id="LC7" class="line"><span class="c"># - Argparse</span></span>&#x000A;<span id="LC8" class="line"><span class="c"># - Phonenumbers</span></span>&#x000A;<span id="LC9" class="line"></span>&#x000A;<span id="LC10" class="line"><span class="kn">from</span> <span class="nn">jinja2</span> <span class="kn">import</span> <span class="n">Environment</span><span class="p">,</span> <span class="n">FileSystemLoader</span></span>&#x000A;<span id="LC11" class="line"><span class="kn">from</span> <span class="nn">colorama</span> <span class="kn">import</span> <span class="n">Fore</span><span class="p">,</span> <span class="n">Style</span></span>&#x000A;<span id="LC12" class="line"><span class="kn">import</span> <span class="nn">argparse</span></span>&#x000A;<span id="LC13" class="line"><span class="kn">import</span> <span class="nn">os</span></span>&#x000A;<span id="LC14" class="line"><span class="kn">import</span> <span class="nn">phonenumbers</span></span>&#x000A;<span id="LC15" class="line"></span>&#x000A;<span id="LC16" class="line"></span>&#x000A;<span id="LC17" class="line"><span class="c"># Get template directory</span></span>&#x000A;<span id="LC18" class="line"><span class="n">TEMPLATE_DIR</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">dirname</span><span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">abspath</span><span class="p">(</span><span class="n">__file__</span><span class="p">))</span></span>&#x000A;<span id="LC19" class="line"><span class="n">TEMPLATE_FILE</span> <span class="o">=</span> <span class="s">&quot;O_signature.tmpl&quot;</span></span>&#x000A;<span id="LC20" class="line"><span class="n">SIGNATURE_DIR</span> <span class="o">=</span> <span class="n">TEMPLATE_DIR</span></span>&#x000A;<span id="LC21" class="line"></span>&#x000A;<span id="LC22" class="line"><span class="c"># Job array</span></span>&#x000A;<span id="LC23" class="line"><span class="n">JOB</span> <span class="o">=</span> <span class="p">{</span><span class="s">&#39;admin&#39;</span><span class="p">:</span> <span class="p">{</span><span class="s">&#39;fr&#39;</span><span class="p">:</span> <span class="s">&quot;Ing&amp;eacute;nieur Syst&amp;egrave;me&quot;</span><span class="p">,</span> <span class="s">&#39;en&#39;</span><span class="p">:</span> <span class="s">&quot;System engineer&quot;</span><span class="p">},</span></span>&#x000A;<span id="LC24" class="line">       <span class="s">&#39;dev&#39;</span><span class="p">:</span> <span class="p">{</span><span class="s">&#39;fr&#39;</span><span class="p">:</span> <span class="s">&quot;Ing&amp;eacute;nieur de Développement&quot;</span><span class="p">,</span> <span class="s">&#39;en&#39;</span><span class="p">:</span> <span class="s">&quot;Software engineer&quot;</span><span class="p">},</span></span>&#x000A;<span id="LC25" class="line">       <span class="s">&#39;design&#39;</span><span class="p">:</span> <span class="p">{</span><span class="s">&#39;fr&#39;</span><span class="p">:</span> <span class="s">&quot;Webdesigner - Int&amp;eacute;grateur&quot;</span><span class="p">,</span> <span class="s">&#39;en&#39;</span><span class="p">:</span> <span class="s">&quot;Web developer&quot;</span><span class="p">},</span></span>&#x000A;<span id="LC26" class="line">       <span class="s">&#39;chef_projet&#39;</span><span class="p">:</span> <span class="p">{</span><span class="s">&#39;fr&#39;</span><span class="p">:</span> <span class="s">&quot;Chef de projet&quot;</span><span class="p">,</span> <span class="s">&#39;en&#39;</span><span class="p">:</span> <span class="s">&quot;Project manager&quot;</span><span class="p">},</span></span>&#x000A;<span id="LC27" class="line">       <span class="s">&#39;consultant&#39;</span><span class="p">:</span> <span class="p">{</span><span class="s">&#39;fr&#39;</span><span class="p">:</span> <span class="s">&quot;Consultant&quot;</span><span class="p">,</span> <span class="s">&#39;en&#39;</span><span class="p">:</span> <span class="s">&quot;Network Junior Administrator&quot;</span><span class="p">},</span></span>&#x000A;<span id="LC28" class="line">       <span class="s">&#39;qualite&#39;</span><span class="p">:</span> <span class="p">{</span><span class="s">&#39;fr&#39;</span><span class="p">:</span> <span class="s">&quot;Ing&amp;eacute;nieur Qualit&amp;eacute;&quot;</span><span class="p">,</span> <span class="s">&#39;en&#39;</span><span class="p">:</span> <span class="s">&quot;Quality engineer&quot;</span><span class="p">}</span></span>&#x000A;<span id="LC29" class="line">       <span class="p">}</span></span>&#x000A;<span id="LC30" class="line"></span>&#x000A;<span id="LC31" class="line"><span class="c"># Create signature file</span></span>&#x000A;<span id="LC32" class="line"><span class="k">class</span> <span class="nc">Signature</span><span class="p">:</span></span>&#x000A;<span id="LC33" class="line">    <span class="c"># Init the class with signature template</span></span>&#x000A;<span id="LC34" class="line">    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">template_directory</span><span class="p">,</span> <span class="n">template_file</span><span class="p">):</span></span>&#x000A;<span id="LC35" class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">template_directory</span> <span class="o">=</span> <span class="n">template_directory</span></span>&#x000A;<span id="LC36" class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">template_file</span> <span class="o">=</span> <span class="n">template_file</span></span>&#x000A;<span id="LC37" class="line"></span>&#x000A;<span id="LC38" class="line">    <span class="c"># Gen html signature</span></span>&#x000A;<span id="LC39" class="line">    <span class="k">def</span> <span class="nf">gen_signature</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">name</span><span class="p">,</span> <span class="n">surname</span><span class="p">,</span> <span class="n">job</span><span class="p">,</span> <span class="n">phone_number</span><span class="p">):</span></span>&#x000A;<span id="LC40" class="line">        <span class="c"># Load template html</span></span>&#x000A;<span id="LC41" class="line">        <span class="n">template</span> <span class="o">=</span> <span class="n">Environment</span><span class="p">(</span><span class="n">loader</span><span class="o">=</span><span class="n">FileSystemLoader</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">template_directory</span><span class="p">))</span><span class="o">.</span><span class="n">get_template</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">template_file</span><span class="p">)</span></span>&#x000A;<span id="LC42" class="line"></span>&#x000A;<span id="LC43" class="line">        <span class="c"># Reformat phone number</span></span>&#x000A;<span id="LC44" class="line">        <span class="n">phone_number</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">set_phonenumber</span><span class="p">(</span><span class="n">phone_number</span><span class="p">)[</span><span class="mi">1</span><span class="p">:]</span></span>&#x000A;<span id="LC45" class="line"></span>&#x000A;<span id="LC46" class="line">        <span class="c"># Print signature</span></span>&#x000A;<span id="LC47" class="line">        <span class="k">return</span> <span class="n">template</span><span class="o">.</span><span class="n">render</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="n">name</span><span class="o">.</span><span class="n">title</span><span class="p">(),</span></span>&#x000A;<span id="LC48" class="line">                               <span class="n">surname</span><span class="o">=</span><span class="n">surname</span><span class="p">,</span></span>&#x000A;<span id="LC49" class="line">                               <span class="n">job_fr</span><span class="o">=</span><span class="n">job</span><span class="p">[</span><span class="s">&#39;fr&#39;</span><span class="p">],</span></span>&#x000A;<span id="LC50" class="line">                               <span class="n">job_en</span><span class="o">=</span><span class="n">job</span><span class="p">[</span><span class="s">&#39;en&#39;</span><span class="p">],</span></span>&#x000A;<span id="LC51" class="line">                               <span class="n">phone_number</span><span class="o">=</span><span class="n">phone_number</span><span class="p">,</span></span>&#x000A;<span id="LC52" class="line">                               <span class="n">email</span><span class="o">=</span><span class="n">name</span> <span class="o">+</span> <span class="s">&quot;.&quot;</span> <span class="o">+</span> <span class="n">surname</span><span class="p">)</span></span>&#x000A;<span id="LC53" class="line"></span>&#x000A;<span id="LC54" class="line">    <span class="nd">@staticmethod</span></span>&#x000A;<span id="LC55" class="line">    <span class="k">def</span> <span class="nf">set_phonenumber</span><span class="p">(</span><span class="n">phone_number</span><span class="p">):</span></span>&#x000A;<span id="LC56" class="line">        <span class="n">phone</span> <span class="o">=</span> <span class="n">phonenumbers</span><span class="o">.</span><span class="n">parse</span><span class="p">(</span><span class="n">phone_number</span><span class="p">,</span> <span class="s">&quot;FR&quot;</span><span class="p">)</span></span>&#x000A;<span id="LC57" class="line">        <span class="k">return</span> <span class="n">phonenumbers</span><span class="o">.</span><span class="n">format_number</span><span class="p">(</span><span class="n">phone</span><span class="p">,</span> <span class="n">phonenumbers</span><span class="o">.</span><span class="n">PhoneNumberFormat</span><span class="o">.</span><span class="n">NATIONAL</span><span class="p">)</span></span>&#x000A;<span id="LC58" class="line"></span>&#x000A;<span id="LC59" class="line"><span class="c"># Define output format</span></span>&#x000A;<span id="LC60" class="line"><span class="k">def</span> <span class="nf">log4py</span><span class="p">(</span><span class="n">text</span><span class="p">,</span> <span class="n">loglvl</span><span class="p">):</span></span>&#x000A;<span id="LC61" class="line">    <span class="k">if</span> <span class="n">loglvl</span> <span class="o">==</span> <span class="s">&quot;CRITI&quot;</span><span class="p">:</span></span>&#x000A;<span id="LC62" class="line">        <span class="k">print</span><span class="p">(</span><span class="n">Fore</span><span class="o">.</span><span class="n">RED</span> <span class="o">+</span> <span class="s">&quot;[CRITICAL] &quot;</span> <span class="o">+</span> <span class="n">Style</span><span class="o">.</span><span class="n">RESET_ALL</span> <span class="o">+</span> <span class="n">text</span><span class="p">)</span></span>&#x000A;<span id="LC63" class="line">    <span class="k">elif</span> <span class="n">loglvl</span> <span class="o">==</span> <span class="s">&quot;WARN&quot;</span><span class="p">:</span></span>&#x000A;<span id="LC64" class="line">        <span class="k">print</span><span class="p">(</span><span class="n">Fore</span><span class="o">.</span><span class="n">YELLOW</span> <span class="o">+</span> <span class="s">&quot;[WARNNING] &quot;</span> <span class="o">+</span> <span class="n">Style</span><span class="o">.</span><span class="n">RESET_ALL</span> <span class="o">+</span> <span class="n">text</span><span class="p">)</span></span>&#x000A;<span id="LC65" class="line">    <span class="k">else</span><span class="p">:</span></span>&#x000A;<span id="LC66" class="line">        <span class="k">print</span><span class="p">(</span><span class="n">Fore</span><span class="o">.</span><span class="n">GREEN</span> <span class="o">+</span> <span class="s">&quot;[INFO] &quot;</span> <span class="o">+</span> <span class="n">Style</span><span class="o">.</span><span class="n">RESET_ALL</span> <span class="o">+</span> <span class="n">text</span><span class="p">)</span></span>&#x000A;<span id="LC67" class="line"></span>&#x000A;<span id="LC68" class="line"><span class="c"># Parse option</span></span>&#x000A;<span id="LC69" class="line"><span class="n">opt_parser</span> <span class="o">=</span> <span class="n">argparse</span><span class="o">.</span><span class="n">ArgumentParser</span><span class="p">(</span><span class="n">description</span><span class="o">=</span><span class="s">&#39;Generate html signature.&#39;</span><span class="p">)</span></span>&#x000A;<span id="LC70" class="line"><span class="n">opt_parser</span><span class="o">.</span><span class="n">add_argument</span><span class="p">(</span><span class="s">&quot;-n&quot;</span><span class="p">,</span> <span class="s">&quot;--name&quot;</span><span class="p">,</span> <span class="n">help</span><span class="o">=</span><span class="s">&quot;Name&quot;</span><span class="p">,</span> <span class="n">action</span><span class="o">=</span><span class="s">&quot;store&quot;</span><span class="p">)</span></span>&#x000A;<span id="LC71" class="line"><span class="n">opt_parser</span><span class="o">.</span><span class="n">add_argument</span><span class="p">(</span><span class="s">&quot;-s&quot;</span><span class="p">,</span> <span class="s">&quot;--surname&quot;</span><span class="p">,</span> <span class="n">help</span><span class="o">=</span><span class="s">&quot;Surname&quot;</span><span class="p">,</span> <span class="n">action</span><span class="o">=</span><span class="s">&quot;store&quot;</span><span class="p">)</span></span>&#x000A;<span id="LC72" class="line"><span class="n">opt_parser</span><span class="o">.</span><span class="n">add_argument</span><span class="p">(</span><span class="s">&quot;-p&quot;</span><span class="p">,</span> <span class="s">&quot;--phone&quot;</span><span class="p">,</span> <span class="n">help</span><span class="o">=</span><span class="s">&quot;Phone Number&quot;</span><span class="p">,</span> <span class="n">action</span><span class="o">=</span><span class="s">&quot;store&quot;</span><span class="p">)</span></span>&#x000A;<span id="LC73" class="line"></span>&#x000A;<span id="LC74" class="line"><span class="c"># Create args object</span></span>&#x000A;<span id="LC75" class="line"><span class="n">args</span> <span class="o">=</span> <span class="n">opt_parser</span><span class="o">.</span><span class="n">parse_args</span><span class="p">()</span></span>&#x000A;<span id="LC76" class="line"></span>&#x000A;<span id="LC77" class="line"><span class="c"># If none argument is set</span></span>&#x000A;<span id="LC78" class="line"><span class="k">if</span> <span class="n">args</span><span class="o">.</span><span class="n">name</span> <span class="ow">is</span> <span class="bp">None</span> <span class="ow">or</span> <span class="n">args</span><span class="o">.</span><span class="n">surname</span> <span class="ow">is</span> <span class="bp">None</span> <span class="ow">or</span> <span class="n">args</span><span class="o">.</span><span class="n">phone</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></span>&#x000A;<span id="LC79" class="line">    <span class="n">opt_parser</span><span class="o">.</span><span class="n">print_help</span><span class="p">()</span></span>&#x000A;<span id="LC80" class="line">    <span class="nb">exit</span><span class="p">(</span><span class="mi">2</span><span class="p">)</span></span>&#x000A;<span id="LC81" class="line"></span>&#x000A;<span id="LC82" class="line"><span class="c"># Init the object with template directory and template file</span></span>&#x000A;<span id="LC83" class="line"><span class="n">signature</span> <span class="o">=</span> <span class="n">Signature</span><span class="p">(</span><span class="n">TEMPLATE_DIR</span><span class="p">,</span> <span class="n">TEMPLATE_FILE</span><span class="p">)</span></span>&#x000A;<span id="LC84" class="line"></span>&#x000A;<span id="LC85" class="line"><span class="n">log4py</span><span class="p">(</span><span class="s">&quot;Set user job.&quot;</span><span class="p">,</span> <span class="s">&quot;OK&quot;</span><span class="p">)</span></span>&#x000A;<span id="LC86" class="line"></span>&#x000A;<span id="LC87" class="line"><span class="c"># Set job</span></span>&#x000A;<span id="LC88" class="line"><span class="k">for</span> <span class="n">key</span> <span class="ow">in</span> <span class="n">JOB</span><span class="p">:</span></span>&#x000A;<span id="LC89" class="line">    <span class="k">print</span><span class="p">(</span><span class="s">&quot;- &quot;</span> <span class="o">+</span> <span class="n">key</span><span class="p">)</span></span>&#x000A;<span id="LC90" class="line"></span>&#x000A;<span id="LC91" class="line"><span class="c"># Get user value</span></span>&#x000A;<span id="LC92" class="line"><span class="n">job_key</span> <span class="o">=</span> <span class="nb">input</span><span class="p">(</span><span class="s">&quot;Please copy and past the job value: &quot;</span><span class="p">)</span></span>&#x000A;<span id="LC93" class="line"></span>&#x000A;<span id="LC94" class="line"><span class="n">log4py</span><span class="p">(</span><span class="n">job_key</span> <span class="o">+</span> <span class="s">&quot; job Selected.&quot;</span><span class="p">,</span> <span class="s">&quot;OK&quot;</span><span class="p">)</span></span>&#x000A;<span id="LC95" class="line"></span>&#x000A;<span id="LC96" class="line"><span class="c"># Test job key</span></span>&#x000A;<span id="LC97" class="line"><span class="k">try</span><span class="p">:</span></span>&#x000A;<span id="LC98" class="line">    <span class="n">JOB</span><span class="p">[</span><span class="n">job_key</span><span class="p">]</span></span>&#x000A;<span id="LC99" class="line"><span class="k">except</span> <span class="nb">KeyError</span><span class="p">:</span></span>&#x000A;<span id="LC100" class="line">    <span class="n">log4py</span><span class="p">(</span><span class="s">&quot;Bad job value.&quot;</span><span class="p">,</span> <span class="s">&quot;CRITI&quot;</span><span class="p">)</span></span>&#x000A;<span id="LC101" class="line">    <span class="nb">exit</span><span class="p">(</span><span class="mi">2</span><span class="p">)</span></span>&#x000A;<span id="LC102" class="line"></span>&#x000A;<span id="LC103" class="line"><span class="c"># Write signature</span></span>&#x000A;<span id="LC104" class="line"><span class="k">try</span><span class="p">:</span></span>&#x000A;<span id="LC105" class="line">    <span class="n">signature_file</span> <span class="o">=</span> <span class="n">SIGNATURE_DIR</span> <span class="o">+</span> <span class="s">&quot;/O_&quot;</span> <span class="o">+</span> <span class="n">args</span><span class="o">.</span><span class="n">name</span><span class="o">.</span><span class="n">title</span><span class="p">()</span> <span class="o">+</span> <span class="s">&quot;.html&quot;</span></span>&#x000A;<span id="LC106" class="line">    <span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="n">signature_file</span><span class="p">,</span> <span class="s">&quot;w&quot;</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span></span>&#x000A;<span id="LC107" class="line">        <span class="n">html</span> <span class="o">=</span> <span class="n">signature</span><span class="o">.</span><span class="n">gen_signature</span><span class="p">(</span><span class="n">args</span><span class="o">.</span><span class="n">name</span><span class="p">,</span> <span class="n">args</span><span class="o">.</span><span class="n">surname</span><span class="p">,</span> <span class="n">JOB</span><span class="p">[</span><span class="n">job_key</span><span class="p">],</span> <span class="n">args</span><span class="o">.</span><span class="n">phone</span><span class="p">)</span></span>&#x000A;<span id="LC108" class="line">        <span class="n">f</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">html</span><span class="p">)</span></span>&#x000A;<span id="LC109" class="line">        <span class="n">f</span><span class="o">.</span><span class="n">close</span><span class="p">()</span></span>&#x000A;<span id="LC110" class="line"><span class="k">except</span><span class="p">:</span></span>&#x000A;<span id="LC111" class="line">    <span class="n">log4py</span><span class="p">(</span><span class="s">&quot;Failed to create signature.&quot;</span><span class="p">,</span> <span class="s">&quot;CRITI&quot;</span><span class="p">)</span></span>&#x000A;<span id="LC112" class="line">    <span class="nb">exit</span><span class="p">(</span><span class="mi">2</span><span class="p">)</span></span>&#x000A;<span id="LC113" class="line"></span>&#x000A;<span id="LC114" class="line"><span class="n">log4py</span><span class="p">(</span><span class="s">&quot;Signature &quot;</span> <span class="o">+</span> <span class="n">signature_file</span> <span class="o">+</span> <span class="s">&quot; is created&quot;</span><span class="p">,</span> <span class="s">&quot;OK&quot;</span><span class="p">)</span></span></code></pre>&#x000A;
</div>

</div>

</article>
</div>

</div>
<div class='modal hide' id='modal-remove-blob'>
<div class='modal-dialog'>
<div class='modal-content'>
<div class='modal-header'>
<a class='close' data-dismiss='modal' href='#'>×</a>
<h3 class='page-title'>Remove gen-orchestra-signature.py</h3>
<p class='light'>
From branch
<strong>master</strong>
</p>
</div>
<div class='modal-body'>
<form accept-charset="UTF-8" action="/Exploit/signatureGenerator/blob/master/gen-orchestra-signature.py" class="form-horizontal" method="post"><div style="display:none"><input name="utf8" type="hidden" value="&#x2713;" /><input name="_method" type="hidden" value="delete" /><input name="authenticity_token" type="hidden" value="dbVUpZ17FD78NRcLVTadqJrzF3oUMxwzEz1zrUjc+GY=" /></div>
<div class='form-group commit_message-group'>
<label class="control-label" for="commit_message">Commit message
</label><div class='col-sm-10'>
<div class='commit-message-container'>
<div class='max-width-marker'></div>
<textarea class="form-control" id="commit_message" name="commit_message" placeholder="Removed this file because..." required="required" rows="3">
</textarea>
</div>
</div>
</div>

<div class='form-group'>
<div class='col-sm-2'></div>
<div class='col-sm-10'>
<button class="btn btn-remove btn-remove-file" name="button" type="submit">Remove file</button>
<a class="btn btn-cancel" data-dismiss="modal" href="#">Cancel</a>
</div>
</div>
</form>

</div>
</div>
</div>
</div>
<script>
  disableButtonIfEmptyField('#commit_message', '.btn-remove-file')
</script>


</div>
</div>
</div>
</div>
</div>

<script>
  (function() {
    $('.page-sidebar-collapsed .nav-sidebar a').tooltip({
      placement: "right"
    });
  
  }).call(this);
</script>

</body>
</html>
