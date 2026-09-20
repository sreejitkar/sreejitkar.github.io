## #1 Where has value accrued in Gen AI so far?

It’s been 18 months since the “iPhone moment of AI”1 but the pace of developments has not slowed down. One of the biggest questions I’ve been thinking about is where does value accrue in Gen AI - today and in the future. 

Today, the Gen AI stack seems to be A-shaped vs V-shaped for cloud2: 

Thanks for reading Apoorv’s notes! Subscribe for free to receive new posts and support my work.

[![](https://substackcdn.com/image/fetch/$s_!actQ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F798fdcd1-736b-4f82-9ea4-a8f7f02cfd86_1600x682.png)](https://substackcdn.com/image/fetch/$s_!actQ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F798fdcd1-736b-4f82-9ea4-a8f7f02cfd86_1600x682.png)

I split the stack into three layers - semis, infra and applications. Here’s a tally of the Gen AI revenues:

  * Semi: Nvidia earned ~$18B of data center revenues in the last reported quarter (ending Jan 2024). Given they have 95%+ market share, let’s estimate ~$75B in annualized revenue for this part of the stack

  * Infra: This layer would have hyperscalers (AWS, GCP, Azure) and the prominent inference clouds (Coreweave, Lambda, etc.). Generously estimate this layer at ~$10B in annualized revenue 

  * Applications: Large language models ([OpenAI](https://www.reuters.com/technology/openai-hits-2-bln-revenue-milestone-ft-2024-02-09/), Anthropic, xAI, et al), image models ([Midjourney](https://www.theinformation.com/briefings/ai-startup-midjourney-expects-200-million-in-revenue?rc=5h8vss) et al), and other pure play generative AI applications. Some Gen AI use-cases might earn revenue disguised as “software” revenues, so for now I estimate this layer generously at ~$5B of annualized revenues 




In contrast, the cloud economy exhibits a much “intuitive” value distribution where the applications closest to the more end-customer earn the most value. 

**Bottom Line: The semis layer has captured ~83% ($75B of $90B revenues) of the Gen AI stack today.** This is much higher than the ~10% that semis capture in the cloud stack today! 

## #2 Where have profits accrued in Gen AI so far?

We get an inverted stack for profitability as well, with semis extracting the highest share today3:

[![](https://substackcdn.com/image/fetch/$s_!G0pN!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5781576b-38f7-4569-aa15-e44ed7f77466_1600x681.png)](https://substackcdn.com/image/fetch/$s_!G0pN!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5781576b-38f7-4569-aa15-e44ed7f77466_1600x681.png)

Here’s the tally:

  * Apps: Anthropic is [estimated](https://www.theinformation.com/articles/anthropics-gross-margin-flags-long-term-ai-profit-questions?rc=5h8vss) to earn ~50-55% gross margins. I assume the same for the overall layer

  * Infra: I estimate the infra players earn ~65% GMs (without including GPU depreciation). If you include depreciation, that number drops to 25-30%

  * Semis: NVIDIA is [estimated](https://www.semianalysis.com/p/nvidia-b100-b200-gb200-cogs-pricing) to earn upwards of ~85% gross margins on their gen AI datacenter products. 

  * The cloud stack is [well](https://www.meritechcapital.com/benchmarking/comps-table#/public-comparables/enterprise/valuation-metrics) [studied](https://www.cnbc.com/2022/12/21/google-leaked-doc-microsoft-azure-losing-money-on-29-bln-in-revenue.html) with the exception of hyperscale gross margins. Azure is [estimated](https://www.cnbc.com/2022/12/21/google-leaked-doc-microsoft-azure-losing-money-on-29-bln-in-revenue.html) to earn ~63% GMs and we assume that for all the infra layer 




Putting it together, the gross profits are significantly concentrated at the semis layer extracting $64B (out of $73B total). Visualizing this below (revenue x gross margin %) : 

[![](https://substackcdn.com/image/fetch/$s_!HTA7!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fadbc5a93-2cf4-47ab-8425-49713870e3d2_1600x703.png)](https://substackcdn.com/image/fetch/$s_!HTA7!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fadbc5a93-2cf4-47ab-8425-49713870e3d2_1600x703.png)

It’s worth visualizing this on a bar chart to intuit the staggering relative proportions. If 100% represents the total gross profits in the system. 

[![](https://substackcdn.com/image/fetch/$s_!C5uO!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F12e639b3-414f-4fa1-bfc1-ea7c588a46c2_698x888.png)](https://substackcdn.com/image/fetch/$s_!C5uO!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F12e639b3-414f-4fa1-bfc1-ea7c588a46c2_698x888.png)

**Bottom line: semis layer has captured ~88% of all gross profits in the Gen AI** **ecosystem (vs 5% for semis in the cloud stack).**

## #3 Where do we go from here? 

We are in early phases of a platform shift where semis capture most of the value. I don’t expect the current structure of Gen AI revenues (inverted pyramid) to stay this way forever. I expect the application layer to capture a similarly high proportion of the value chain in due time. 

Here is a case study of how the value accrued in the mobile wave. Over a the last decade the value in mobile accrued first in semis, then in infra layer, and finally at the software layer: 

[![](https://substackcdn.com/image/fetch/$s_!Ll5B!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7d8d1198-e120-4cad-9c0a-af054c59d82e_1792x1114.png)](https://substackcdn.com/image/fetch/$s_!Ll5B!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7d8d1198-e120-4cad-9c0a-af054c59d82e_1792x1114.png)

Similarly in the cloud, we first witnessed a datacenter buildout followed by the rise of the cloud service providers. AWS started in 2004 and got its first customers in 2010-12 (Amazon itself switched to AWS in 2010 and in 2012 Netflix joined them). 

In similar fashion, I expect Gen AI to follow suit. We are in Inning #1 (Semis) and I expect we’ll get to Inning 3 (Applications) by the end of the decade. As a corollary, given we are stating a low base, I see the biggest open opportunity to be in the application stack! 

[![](https://substackcdn.com/image/fetch/$s_!LP3U!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd9b7d14a-68c2-424e-895e-235b78c53aad_1600x722.png)](https://substackcdn.com/image/fetch/$s_!LP3U!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd9b7d14a-68c2-424e-895e-235b78c53aad_1600x722.png)

There are a few critical questions along the way on this transition that I think about: 

#### **A) Will NVIDIA continue to extract 85%+ gross margins?**  

I believe not. It appears that **NVIDIA’s margins have peaked** and are on a downward trajectory. From [SemiAnalysis](https://www.semianalysis.com/p/nvidia-b100-b200-gb200-cogs-pricing):_“We believe NVIDIA’s margins have peaked. We expect B100 and future families to have slightly lower margins, but furthermore, over the next few quarters H100 margins will also come down due to the H200 and H20.”_

The key question I track as leading indicators of NVIDIA supremacy are: 

  1. Lead times for GPU supply? Currently ~6 weeks

  2. Trends in GPU rental prices? ([Pricing sheet here](https://www.coreweave.com/gpu-cloud-pricing))




#### **B) Cloud apps earn 75-80% GMs but AI apps earn 0-50% margins, how will that evolve?  
**  


**I believe AI apps will have improve profitability over time.** There are a few levers that that will help drive better profitability in the future 

  * Better pricing / value alignment: it’s widely known that In [some cases](https://news.ycombinator.com/item?id=37827955), they are not profitable at all - especially for power users given the COGS are linked to the amount of usage.

  * Custom silicon chips → lower TCO: all the hyperscalers and Meta are working on their own versions of semiconductors ([Google](https://cloud.google.com/tpu), [Microsoft](https://www.theverge.com/2023/11/15/23960345/microsoft-cpu-gpu-ai-chips-azure-maia-cobalt-specifications-cloud-infrastructure), [Amazon](https://aws.amazon.com/silicon-innovation/), and [Meta](https://engineering.fb.com/2023/10/18/ml-applications/meta-ai-custom-silicon-olivia-wu/)). In due time, this should reduce total cost of ownership (TCO) not only because it will remove the margin stacking but also because allow them to specialize on workloads 

  * Improvements in model architecture: I am seeing various non-transformer approaches such as state-space models (good for long context window use-cases such as coding), JEPA (good for video models), etc. 

  * Reduction in model costs: driven by various techniques such as [batching](https://twitter.com/openaidevs/status/1779922566091522492?s=46), distillation, quantization, mixture of experts, etc. models are getting cheaper at a rapid pace. As [Bill Gurley points out](https://twitter.com/bgurley/status/1774896120310686003): 




[![](https://substackcdn.com/image/fetch/$s_!0HbY!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffc47032f-2d2e-4eb4-a226-8964d9b469ec_1168x1718.png)](https://substackcdn.com/image/fetch/$s_!0HbY!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffc47032f-2d2e-4eb4-a226-8964d9b469ec_1168x1718.png)

#### **C) What about Gen AI in consumer?**  

I expect a similar transition in consumer starting from the hardware layer. Much like the data center, consumer devices will be upgraded to AI PC / Smartphone / novel form factors (e.g. Meta glasses, Humane Pin, Rabbit R1). Consumer applications have three segments: information (search), entertainment (gaming, media), and transaction (travel, e-com etc.). Search queries are increasingly moving from informational to LLM-based searches, as my colleague [Vivek](https://twitter.com/Goyal_Vivek) calculates: 

[![](https://substackcdn.com/image/fetch/$s_!xdRF!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F54a9fca8-b8ea-4240-9a73-dc6a2c25f11b_1268x866.png)](https://substackcdn.com/image/fetch/$s_!xdRF!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F54a9fca8-b8ea-4240-9a73-dc6a2c25f11b_1268x866.png)

[![](https://substackcdn.com/image/fetch/$s_!Zxif!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff2485baf-f84f-465b-8cc9-cba48d2f8585_1300x918.png)](https://substackcdn.com/image/fetch/$s_!Zxif!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff2485baf-f84f-465b-8cc9-cba48d2f8585_1300x918.png)

Similarly in entertainment: between gaming and media both we expect value to shift from creators/producers to tech enablers. Again from my colleague [Vivek](https://twitter.com/Goyal_Vivek): 

[![](https://substackcdn.com/image/fetch/$s_!TsIA!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0d55d6e8-5907-414f-8d81-203c4221c834_1258x878.png)](https://substackcdn.com/image/fetch/$s_!TsIA!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0d55d6e8-5907-414f-8d81-203c4221c834_1258x878.png)

_Thanks to Brad Gerstner, Sud Bhatija, Sanjiv Kalevar, Cobi B-Gantz, Omar Shaya, Jamin Ball, Vivek Goyal and Shreya Bhargava for their input on this article.  _

* * *

The information presented in this newsletter is the opinion of the author and does not necessarily reflect the view of any other person or entity, including Altimeter Capital Management, LP ("Altimeter"). The information provided is believed to be from reliable sources but no liability is accepted for any inaccuracies. This is for information purposes and should not be construed as an investment recommendation. Past performance is no guarantee of future performance. Altimeter is an investment adviser registered with the U.S. Securities and Exchange Commission. Registration does not imply a certain level of skill or training.

This post and the information presented are intended for informational purposes only. The views expressed herein are the author’s alone and do not constitute an offer to sell, or a recommendation to purchase, or a solicitation of an offer to buy, any security, nor a recommendation for any investment product or service. While certain information contained herein has been obtained from sources believed to be reliable, neither the author nor any of his employers or their affiliates have independently verified this information, and its accuracy and completeness cannot be guaranteed. Accordingly, no representation or warranty, express or implied, is made as to, and no reliance should be placed on, the fairness, accuracy, timeliness or completeness of this information. The author and all employers and their affiliated persons assume no liability for this information and no obligation to update the information or analysis contained herein in the future.

1

Source:  [Jensen Huang](https://www.youtube.com/watch?v=3O4OujSFwt8)

2

Sources: 1) Semi layer revenue based on Q4’24 NVIDIA data center revenues of $18.4B annualized. 2) Infra and App layer revenue based on internal estimates. 3) Cloud stack revenue based on Coatue [analysis](https://www.coatue.com/blog/perspective/ai-the-coming-revolution-2023)

3

Sources: 1) AI Semi [source](https://x.com/firstadopter/status/1691638727951397012), 2) AI Infra layer GM based on internal estimates (65% does not include depreciation), 3) AI app [source](https://www.theinformation.com/articles/anthropics-gross-margin-flags-long-term-ai-profit-questions?rc=5h8vss) 4) Cloud Semi GM based on Intel + AMD CY2023 results, 5) Cloud Infra GMs [source](https://www.cnbc.com/2022/12/21/google-leaked-doc-microsoft-azure-losing-money-on-29-bln-in-revenue.html), 6) Cloud apps [Meritech analysis](https://www.meritechcapital.com/benchmarking/comps-table#/public-comparables/enterprise/valuation-metrics)
