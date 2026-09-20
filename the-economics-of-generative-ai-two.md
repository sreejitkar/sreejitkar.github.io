I am excited to update my original analysis from 2024: [The Economics of Generative AI](https://apoorv03.com/p/the-economics-of-generative-ai). This is the analysis I come back to more than anything else I’ve written because it’s a reminder of the “physics” of the AI industry.

Two years ago, I found that the Gen AI value chain was inverted: the compute layer captured ~83% of all revenue and ~87% of all gross profit. The application layer, despite being closest to end customers, earned almost nothing. I predicted this would flip over time, following the pattern of every prior platform shift. Two years ago, I said:

[![](https://substackcdn.com/image/fetch/$s_!CADs!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F48e9c94a-881a-4148-945f-8475bb485737_2048x955.png)](https://substackcdn.com/image/fetch/$s_!CADs!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F48e9c94a-881a-4148-945f-8475bb485737_2048x955.png)

Two years since, the AI ecosystem has grown roughly 5x, from ~$90B to ~$435B in annualized revenue. But what’s remarkable is how little the shape of economics has changed.

**The bottom line upfront: Semi is a one-player game. Apps is a two-player game. Infra is the only competitive layer. The most profitable strategy in AI is still selling the shovels. :)**

Let’s dig in!

## **#1 The value chain is still inverted**

[![](https://substackcdn.com/image/fetch/$s_!T85K!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0310bf44-2cfe-403a-a702-62cc7e499f48_2030x926.png)](https://substackcdn.com/image/fetch/$s_!T85K!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0310bf44-2cfe-403a-a702-62cc7e499f48_2030x926.png)

Here’s how each layer breaks down:

  * **Semi (~$300B):** This is overwhelmingly NVIDIA. Their data center business did $62B last quarter, annualizing to ~$250B. Broadcom’s AI semi business (custom accelerators for Google, Meta, ByteDance) adds ~$34B. An estimated ~$25B in high bandwidth memory purchased directly by hyperscalers for custom chip programs rounds it out. The concentration is extreme: NVIDIA is ~80% of the layer.

  * **Infra (~$75B):** AI-specific cloud infrastructure. Azure, AWS, GCP, Oracle each contribute $10-20B in AI-attributable revenue. CoreWeave adds ~$6B. Baseten, Together, Modal and other inference providers collectively make up the rest. Unlike the other layers, this one is relatively evenly distributed across the major clouds.

  * **Apps (~$60B):** Also extremely concentrated, but in two companies. OpenAI and Anthropic together make up ~45B annualized revenue and are ~75% of the layer. A distant third are the coding AI players like Cursor, followed by the fast growing agent companies like ElevenLabs, Glean, Sierra, Perplexity, Replit, Lovable, Harvey, Abridge, etc..  





**Bottom line: semi layer still captures ~70% of all AI revenues.** In the cloud stack, semis capture 1/10th that share: ~8%. That gap is the core distortion between this supercycle and the prior one.

## **#2 AI grew 5x but NVIDIA captured most of the value**

Despite 5x growth in the overall ecosystem, the shape hasn’t changed much. The app layer grew fastest in percentage terms (12x in two years). But on absolute dollars, the semi layer added ~$225B vs ~$55B for apps. NVIDIA alone added $175B of incremental revenue. That’s roughly 3x the size of the entire app layer today.

[![](https://substackcdn.com/image/fetch/$s_!v75D!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe5c4d9a9-d4d0-401b-9177-07529e5b6af7_1670x1298.png)](https://substackcdn.com/image/fetch/$s_!v75D!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe5c4d9a9-d4d0-401b-9177-07529e5b6af7_1670x1298.png)

The profitability picture is even more skewed. Semis run at ~73% gross margins. The infra layer runs at ~55%. Apps run at ~33% based on my estimates.

[![](https://substackcdn.com/image/fetch/$s_!F06c!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8df10c62-91e8-457f-bff0-ffd98dc2fe2d_2012x860.png)](https://substackcdn.com/image/fetch/$s_!F06c!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8df10c62-91e8-457f-bff0-ffd98dc2fe2d_2012x860.png)

Multiplying through: the semi layer earns ~$225B in gross profit. Infra earns ~$40B. Apps earn ~$20B. **Semis capture 79% of all gross profit dollars in the AI ecosystem.** For comparison, in the cloud stack apps capture 70% and semis capture 6%. The AI stack is almost exactly the mirror image.

Over two years, infra and apps each gained about 4 points of profit share. Semis went from 87% to 79%. At that pace, it would take well over a decade for the app layer to reach the kind of share that apps enjoy in cloud.

[![](https://substackcdn.com/image/fetch/$s_!YvZD!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F54b528e3-82a4-4e13-bc21-34822c2b7f37_1664x1336.png)](https://substackcdn.com/image/fetch/$s_!YvZD!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F54b528e3-82a4-4e13-bc21-34822c2b7f37_1664x1336.png)

## **#3 The capex question: is it worth it?**

The top five hyperscalers spent [~$443B](https://epoch.ai/data-insights/hyperscaler-capex-trend) in capex in 2025, up 73% from $256B in 2024. That number is projected to exceed $600B in 2026, with roughly [75%](https://techblog.comsoc.org/2025/12/22/hyperscaler-capex-600-bn-in-2026-a-36-increase-over-2025-while-global-spending-on-cloud-infrastructure-services-skyrockets/) (~$450B) directed at AI infrastructure. Which raises the obvious question: **is all this capex generating positive ROI?**

[![](https://substackcdn.com/image/fetch/$s_!iBUK!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa33a36fb-d608-478f-9932-d84986186281_1183x559.png)](https://substackcdn.com/image/fetch/$s_!iBUK!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa33a36fb-d608-478f-9932-d84986186281_1183x559.png)

The CEOs are betting it’s worth it:

  * **Andy Jassy, Amazon** (Q4 2025 earnings call,[ Feb 2026](https://www.cnbc.com/2026/02/05/aws-q4-earnings-report-2025.html)): _“As fast as we’re adding capacity right now, we’re monetizing it.”_

  * **Sundar Pichai, Alphabet** (Q4 2025 earnings call,[ Feb 2026](https://www.cnbc.com/2026/02/04/alphabet-googl-q4-2025-earnings.html)): _“We are seeing our AI investments and infrastructure drive revenue and growth across the board.” Though he also acknowledged “elements of irrationality” in the current scale of AI investing._

  * **Mark Zuckerberg, Meta** (Q4 2025 earnings call,[ Jan 2026](https://www.cnbc.com/2026/01/28/metas-zuckerberg-gets-green-light-from-wall-street-to-invest-in-ai.html)): _“I think it’s the right strategy to aggressively front load building capacity. In the worst case, we would just slow building new infrastructure for some period while we grow into what we build.”_




Here’s what they are buying with all that money. The chart below shows cumulative AI compute capacity by chip type. The answer is overwhelmingly NVIDIA, though non-NVIDIA silicon is starting to show up at the margins:

[![](https://substackcdn.com/image/fetch/$s_!l_3_!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2b4e875a-1015-4982-b064-24a88a6f7d14_2048x1515.png)](https://substackcdn.com/image/fetch/$s_!l_3_!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2b4e875a-1015-4982-b064-24a88a6f7d14_2048x1515.png)

_Source:[ Epoch AI](https://epoch.ai/data-insights/hyperscaler-capex-trend). Cumulative compute capacity measured in H100-equivalents._

Every major hyperscaler is hedging by developing custom silicon. Sorted by maturity:

  * **Google TPU** (most mature): 7th-gen Ironwood now[ generally available](https://www.constellationr.com/blog-news/insights/google-clouds-ironwood-ready-general-availability). Anthropic ordered[ up to 1 million TPU chips](https://nvidianews.nvidia.com/news/rubin-platform-ai-supercomputer), worth tens of billions. Google is now selling TPUs as merchant hardware. Competitive pressure from TPUs has reportedly forced NVIDIA to[ cut pricing ~30%](https://howaiworks.ai/blog/google-tpuv7-ironwood-announcement-2025) for some customers.

  * **Amazon Trainium** (scaling fast):[ 1.4 million Trainium2 chips deployed](https://futurumgroup.com/insights/amazon-q4-fy-2025-revenue-beat-aws-24-amid-200b-capex-plan/), powering majority of Bedrock inference. According to Amazon, custom chips business crossed[ $10B annual run rate](https://futurumgroup.com/insights/amazon-q4-fy-2025-revenue-beat-aws-24-amid-200b-capex-plan/), growing triple digits. Trainium3 (3nm) in production,[ nearly all supply committed](https://fifthperson.com/amazon-q4-2025/) through mid-2026.

  * **OpenAI custom ASICs** (new entrant) + **AMD** : Signed[ multiyear deal with Broadcom](https://www.tomshardware.com/openai-broadcom-to-co-develop-10gw-of-custom-ai-chips) for 10GW of custom accelerators starting 2026. Separately signed[ 6GW deal with AMD](https://www.sec.gov/Archives/edgar/data/0000002488/000000248825000163/q32025991.htm) for Instinct MI450 GPUs.

  * **Microsoft Maia** \+ **AMD** : Deployed[ Maia 200 in Azure](https://techcrunch.com/2026/01/29/microsoft-wont-stop-buying-ai-chips-from-nvidia-amd-even-after-launching-its-own-nadella-says/) (Jan 2026). Claims 3x performance of Trainium3 on inference. Now powering a portion of ChatGPT workloads. Nadella said Microsoft will still buy from NVIDIA and AMD alongside Maia.

  * **Meta MTIA** (internal only): MTIA v3 deployed for internal inference. Acquired chip startup[ Rivos](https://www.sdxcentral.com/news/top-5-hardware-stories-of-2025-broadcom-openai-aws-doubles-down-on-custom-nvidia-marches-on/) (Sept 2025) for RISC-V designs targeting 2026.




Jensen Huang has[ dismissed custom ASICs](https://www.techbrew.com/stories/2025/11/13/custom-ai-chips-gpu-xpu) as “noncompetitive,” noting “a lot of ASICs get canceled.” He’s not wrong historically :)

## **#4 The stack will eventually flip. It may take longer than 10 years.**

I still believe the stack flips eventually. I’m just less sure about when.

[![](https://substackcdn.com/image/fetch/$s_!u1SQ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F98d38ab5-09ee-4d5f-9cfc-68ff00e54026_2048x936.png)](https://substackcdn.com/image/fetch/$s_!u1SQ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F98d38ab5-09ee-4d5f-9cfc-68ff00e54026_2048x936.png)

For the shape to invert, either the app layer needs to keep exploding or the semi layer needs to get cheaper. Both are happening, but neither fast enough to change the shape within this decade.

The cloud stack took roughly 15 years to evolve from hardware-dominated to software-dominated. The AI stack may follow a similar timeline. The custom silicon efforts are the key variable. If TPUs, Trainium and the other ASICs succeed at scale, they could compress NVIDIA’s margins and shift profits up the stack. But outside Google’s TPUs, no custom silicon program has proven it can compete with NVIDIA at scale for training workloads.

The biggest open opportunity remains in the application layer. That’s where I spend most of my time. But investors and builders should be clear-eyed about where the economics sit today. The most profitable company in AI is still the one selling the shovels.

* * *

_For the underlying data behind this analysis, ping me. Happy to share the full datasheet._

_The information presented in this newsletter is the opinion of the author and does not reflect the view of any other person or entity, including Altimeter Capital Management, LP (”Altimeter”). The information provided is believed to be from reliable sources but no liability is accepted for any inaccuracies. This is for informational purposes and should not be construed as investment advice or an investment recommendation. Past performance is no guarantee of future performance. Altimeter is an investment adviser registered with the U.S. Securities and Exchange Commission. Registration does not imply a certain level of skill or training. Altimeter and its clients trade in public securities and have made and/or may make investments in or investment decisions relating to the companies referenced herein. The views expressed herein are those of the author and not of Altimeter or its clients, which reserve the right to make investment decisions or engage in trading activity that would be (or could be construed as) consistent and/or inconsistent with the views expressed herein._

_This post and the information presented are intended for informational purposes only. The views expressed herein are the author’s alone and do not constitute an offer to sell, or a recommendation to purchase, or a solicitation of an offer to buy, any security, nor a recommendation for any investment product or service. While certain information contained herein has been obtained from sources believed to be reliable, neither the author nor any of his employers or their affiliates have independently verified this information, and its accuracy and completeness cannot be guaranteed. Accordingly, no representation or warranty, express or implied, is made as to, and no reliance should be placed on the fairness, accuracy, timeliness or completeness of this information. The author and all employers and their affiliated persons assume no liability for this information and no obligation to update the information or analysis contained herein in the future._
